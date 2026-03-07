import { useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import Fuse from 'fuse.js'
import { Search, X } from 'lucide-react'
import { useStore } from '../stores/useStore'
import { ItemRow } from '../components/ItemRow'

export function SearchView() {
  const { allItems } = useStore()
  const [query, setQuery] = useState('')

  const items = allItems()

  const fuse = useMemo(
    () =>
      new Fuse(items, {
        keys: [
          { name: 'text', weight: 0.6 },
          { name: 'section', weight: 0.2 },
          { name: 'tracker_label', weight: 0.1 },
          { name: 'tags', weight: 0.1 },
        ],
        threshold: 0.35,
        includeScore: true,
        includeMatches: true,
      }),
    [items]
  )

  const results = useMemo(() => {
    if (!query.trim()) return []
    return fuse.search(query).slice(0, 100)
  }, [fuse, query])

  return (
    <motion.div
      key="search"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="h-full flex flex-col"
    >
      {/* Search input */}
      <div className="px-6 py-4 flex-shrink-0" style={{ borderBottom: '1px solid var(--border)' }}>
        <div className="relative max-w-2xl">
          <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-tertiary pointer-events-none" />
          <input
            autoFocus
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search across all trackers…"
            className="input-apple pl-9 pr-9 py-2.5 text-sm"
          />
          {query && (
            <button
              onClick={() => setQuery('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-tertiary hover:text-primary transition-colors"
            >
              <X size={14} />
            </button>
          )}
        </div>
        {query && (
          <p className="text-xs text-tertiary mt-2">
            {results.length} result{results.length !== 1 ? 's' : ''} for "{query}"
          </p>
        )}
      </div>

      {/* Results */}
      <div className="flex-1 overflow-y-auto px-2 py-2">
        <AnimatePresence mode="popLayout">
          {!query && (
            <motion.div
              key="empty"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex flex-col items-center justify-center py-20 text-tertiary"
            >
              <Search size={32} className="mb-3 opacity-30" />
              <div className="text-sm">Start typing to search {items.length} items</div>
              <div className="text-xs mt-1 opacity-60">Searches text, sections, tags, and tracker names</div>
            </motion.div>
          )}

          {query && results.length === 0 && (
            <motion.div
              key="no-results"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex flex-col items-center justify-center py-20 text-tertiary"
            >
              <div className="text-3xl mb-3">🔍</div>
              <div className="text-sm">No results for "{query}"</div>
            </motion.div>
          )}

          {results.map(({ item }) => (
            <motion.div
              key={item.id}
              layout
              initial={{ opacity: 0, y: 4 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
            >
              <ItemRow item={item} showTracker />
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </motion.div>
  )
}
