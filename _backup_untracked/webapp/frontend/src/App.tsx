import { useEffect, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { LayoutGrid, LayoutList, Columns, Search, Menu, X } from 'lucide-react'
import { useStore } from './stores/useStore'
import { Sidebar } from './components/Sidebar'
import { Header } from './components/Header'
import { BoardView } from './views/BoardView'
import { ListView } from './views/ListView'
import { KanbanView } from './views/KanbanView'
import { SearchView } from './views/SearchView'
import type { ViewMode } from './types'
import clsx from 'clsx'

const BOTTOM_NAV: { id: ViewMode; label: string; icon: React.ReactNode }[] = [
  { id: 'board', label: 'Board', icon: <LayoutGrid size={20} /> },
  { id: 'list', label: 'List', icon: <LayoutList size={20} /> },
  { id: 'kanban', label: 'Kanban', icon: <Columns size={20} /> },
  { id: 'search', label: 'Search', icon: <Search size={20} /> },
]

function LoadingScreen() {
  return (
    <div className="flex items-center justify-center h-screen" style={{ background: 'var(--bg)' }}>
      <div className="flex flex-col items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center animate-pulse">
          <span className="text-white font-bold text-lg">B</span>
        </div>
        <div className="text-sm text-secondary">Loading Brain…</div>
      </div>
    </div>
  )
}

function ErrorScreen({ error }: { error: string }) {
  const { fetchTrackers } = useStore()
  return (
    <div className="flex items-center justify-center h-screen" style={{ background: 'var(--bg)' }}>
      <div className="glass-card p-8 max-w-md text-center mx-4">
        <div className="text-3xl mb-3">⚠️</div>
        <h2 className="text-base font-semibold text-primary mb-2">Backend not reachable</h2>
        <p className="text-sm text-secondary mb-4">
          Make sure the FastAPI backend is running on port 8000.
        </p>
        <code className="block text-xs font-mono p-3 rounded-apple-sm mb-4 text-left"
          style={{ background: 'var(--border)' }}>
          cd webapp/backend<br />
          pip install -r requirements.txt<br />
          uvicorn main:app --reload --port 8000
        </code>
        <p className="text-xs text-tertiary mb-4">{error}</p>
        <button onClick={fetchTrackers} className="btn-primary">Retry</button>
      </div>
    </div>
  )
}

export default function App() {
  const { view, setView, loading, error, fetchTrackers, darkMode } = useStore()
  const [sidebarOpen, setSidebarOpen] = useState(false)

  useEffect(() => {
    document.documentElement.classList.toggle('dark', darkMode)
  }, [darkMode])

  useEffect(() => {
    fetchTrackers()
  }, [fetchTrackers])

  if (loading && !error) return <LoadingScreen />
  if (error) return <ErrorScreen error={error} />

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--bg)' }}>
      {/* Desktop sidebar */}
      <div className="hidden md:block">
        <Sidebar />
      </div>

      {/* Mobile sidebar overlay */}
      <AnimatePresence>
        {sidebarOpen && (
          <>
            {/* Backdrop */}
            <motion.div
              key="backdrop"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="fixed inset-0 z-40 md:hidden"
              style={{ background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)' }}
              onClick={() => setSidebarOpen(false)}
            />
            {/* Drawer */}
            <motion.div
              key="drawer"
              initial={{ x: -280 }}
              animate={{ x: 0 }}
              exit={{ x: -280 }}
              transition={{ type: 'spring', damping: 28, stiffness: 300 }}
              className="fixed left-0 top-0 bottom-0 z-50 md:hidden"
              style={{ width: 280 }}
            >
              <Sidebar onClose={() => setSidebarOpen(false)} />
            </motion.div>
          </>
        )}
      </AnimatePresence>

      {/* Main content */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* Mobile header with hamburger */}
        <div className="flex md:hidden items-center gap-3 px-4 py-3 border-b"
          style={{ borderColor: 'var(--border)', background: 'var(--sidebar-bg)' }}>
          <button
            onClick={() => setSidebarOpen(true)}
            className="btn-ghost p-2 rounded-apple-sm -ml-1"
            aria-label="Open menu"
          >
            <Menu size={20} />
          </button>
          <div className="flex items-center gap-2 flex-1">
            <div className="w-6 h-6 rounded-md bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
              <span className="text-white text-[10px] font-bold">B</span>
            </div>
            <span className="text-sm font-semibold text-primary">Beats PM</span>
          </div>
          {/* View title on mobile */}
          <span className="text-sm font-medium text-secondary capitalize">{view}</span>
        </div>

        {/* Desktop header */}
        <div className="hidden md:block">
          <Header />
        </div>

        <main className="flex-1 overflow-hidden pb-safe">
          <AnimatePresence mode="wait">
            {view === 'board' && <BoardView key="board" />}
            {view === 'list' && <ListView key="list" />}
            {view === 'kanban' && <KanbanView key="kanban" />}
            {view === 'search' && <SearchView key="search" />}
          </AnimatePresence>
        </main>

        {/* Mobile bottom navigation */}
        <nav
          className="flex md:hidden items-center justify-around border-t pb-safe-bottom"
          style={{
            borderColor: 'var(--border)',
            background: 'var(--sidebar-bg)',
            backdropFilter: 'blur(20px)',
            WebkitBackdropFilter: 'blur(20px)',
            paddingBottom: 'max(env(safe-area-inset-bottom), 8px)',
          }}
        >
          {BOTTOM_NAV.map((item) => (
            <button
              key={item.id}
              onClick={() => setView(item.id)}
              className={clsx(
                'flex flex-col items-center gap-1 px-4 py-2 rounded-apple-sm transition-all duration-150 min-w-0 flex-1',
                view === item.id ? 'text-accent' : 'text-tertiary'
              )}
              style={{ color: view === item.id ? 'var(--accent)' : 'var(--text-tertiary)' }}
            >
              {item.icon}
              <span className="text-[10px] font-medium">{item.label}</span>
            </button>
          ))}
        </nav>
      </div>
    </div>
  )
}
