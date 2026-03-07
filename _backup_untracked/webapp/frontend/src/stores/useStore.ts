import { create } from 'zustand'
import type { TrackerFile, TrackerItem, ViewMode, FilterState, ItemStatus } from '../types'

const API = '/api'

interface AppState {
  // Data
  trackers: TrackerFile[]
  loading: boolean
  error: string | null

  // View
  view: ViewMode
  filter: FilterState
  selectedTracker: string | null
  darkMode: boolean

  // Actions
  fetchTrackers: () => Promise<void>
  setView: (v: ViewMode) => void
  setFilter: (f: Partial<FilterState>) => void
  setSelectedTracker: (key: string | null) => void
  toggleDarkMode: () => void
  updateItemStatus: (trackerKey: string, itemId: string, status: ItemStatus) => Promise<void>

  // Derived
  allItems: () => TrackerItem[]
  filteredItems: () => TrackerItem[]
}

export const useStore = create<AppState>((set, get) => ({
  trackers: [],
  loading: false,
  error: null,
  view: 'board',
  filter: { status: 'all', tracker: 'all', query: '' },
  selectedTracker: null,
  darkMode: window.matchMedia('(prefers-color-scheme: dark)').matches,

  fetchTrackers: async () => {
    set({ loading: true, error: null })
    try {
      const res = await fetch(`${API}/trackers/`)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data: TrackerFile[] = await res.json()
      set({ trackers: data, loading: false })
    } catch (e) {
      set({ error: String(e), loading: false })
    }
  },

  setView: (view) => set({ view }),
  setFilter: (f) => set((s) => ({ filter: { ...s.filter, ...f } })),
  setSelectedTracker: (key) => set({ selectedTracker: key }),

  toggleDarkMode: () => {
    const next = !get().darkMode
    set({ darkMode: next })
    document.documentElement.classList.toggle('dark', next)
  },

  updateItemStatus: async (trackerKey, itemId, status) => {
    // Optimistic update
    set((s) => ({
      trackers: s.trackers.map((t) =>
        t.key !== trackerKey
          ? t
          : {
              ...t,
              items: t.items.map((i) => (i.id === itemId ? { ...i, status } : i)),
            }
      ),
    }))
    try {
      await fetch(`${API}/trackers/${trackerKey}/items/${itemId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status }),
      })
    } catch {
      // Revert on failure
      get().fetchTrackers()
    }
  },

  allItems: () => get().trackers.flatMap((t) => t.items),

  filteredItems: () => {
    const { filter, trackers } = get()
    let items = trackers.flatMap((t) => t.items)
    if (filter.tracker !== 'all') items = items.filter((i) => i.tracker === filter.tracker)
    if (filter.status !== 'all') items = items.filter((i) => i.status === filter.status)
    if (filter.query) {
      const q = filter.query.toLowerCase()
      items = items.filter(
        (i) =>
          i.text.toLowerCase().includes(q) ||
          (i.section?.toLowerCase().includes(q) ?? false) ||
          i.tags.some((t) => t.toLowerCase().includes(q))
      )
    }
    return items
  },
}))
