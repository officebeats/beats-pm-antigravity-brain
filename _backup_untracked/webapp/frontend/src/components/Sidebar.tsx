import { motion } from 'framer-motion'
import {
  Bug, Star, Scale, FolderOpen, Users, Code2, Palette,
  LayoutList, LayoutGrid, Columns, Search, Moon, Sun, RefreshCw, X,
} from 'lucide-react'
import { useStore } from '../stores/useStore'
import type { ViewMode } from '../types'
import clsx from 'clsx'

const TRACKER_ICONS: Record<string, React.ReactNode> = {
  bugs_master: <Bug size={15} />,
  boss_requests: <Star size={15} />,
  decision_log: <Scale size={15} />,
  projects_master: <FolderOpen size={15} />,
  delegated_tasks: <Users size={15} />,
  eng_tasks: <Code2 size={15} />,
  ux_tasks: <Palette size={15} />,
}

const VIEWS: { id: ViewMode; label: string; icon: React.ReactNode }[] = [
  { id: 'board', label: 'Board', icon: <LayoutGrid size={15} /> },
  { id: 'list', label: 'List', icon: <LayoutList size={15} /> },
  { id: 'kanban', label: 'Kanban', icon: <Columns size={15} /> },
  { id: 'search', label: 'Search', icon: <Search size={15} /> },
]

interface SidebarProps {
  onClose?: () => void
}

export function Sidebar({ onClose }: SidebarProps) {
  const { view, setView, trackers, selectedTracker, setSelectedTracker, darkMode, toggleDarkMode, fetchTrackers, loading } = useStore()

  const handleViewClick = (id: ViewMode) => {
    setView(id)
    onClose?.()
  }

  const handleTrackerClick = (key: string) => {
    setSelectedTracker(key)
    setView('list')
    onClose?.()
  }

  const handleAllTrackers = () => {
    setSelectedTracker(null)
    onClose?.()
  }

  return (
    <motion.aside
      initial={{ x: -20, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ duration: 0.3, ease: [0.34, 1.56, 0.64, 1] }}
      className="w-64 md:w-56 flex-shrink-0 flex flex-col h-full"
      style={{ background: 'var(--sidebar-bg)', borderRight: '1px solid var(--border)' }}
    >
      {/* Logo + close button */}
      <div className="px-4 pt-5 pb-3 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
            <span className="text-white text-xs font-bold">B</span>
          </div>
          <div>
            <div className="text-sm font-semibold text-primary leading-tight">Beats PM</div>
            <div className="text-[10px] text-tertiary leading-tight">Antigravity Brain</div>
          </div>
        </div>
        {onClose && (
          <button
            onClick={onClose}
            className="btn-ghost p-1.5 rounded-apple-sm md:hidden"
            aria-label="Close menu"
          >
            <X size={16} />
          </button>
        )}
      </div>

      {/* Views */}
      <div className="px-2 mb-1">
        <div className="text-[10px] font-semibold uppercase tracking-wider text-tertiary px-2 mb-1">Views</div>
        {VIEWS.map((v) => (
          <button
            key={v.id}
            onClick={() => handleViewClick(v.id)}
            className={clsx('sidebar-item w-full', view === v.id && 'active')}
          >
            {v.icon}
            {v.label}
          </button>
        ))}
      </div>

      <div className="mx-3 my-2" style={{ height: 1, background: 'var(--border)' }} />

      {/* Trackers */}
      <div className="px-2 flex-1 overflow-y-auto">
        <div className="text-[10px] font-semibold uppercase tracking-wider text-tertiary px-2 mb-1">Trackers</div>
        <button
          onClick={handleAllTrackers}
          className={clsx('sidebar-item w-full', selectedTracker === null && view !== 'search' && 'active')}
        >
          <LayoutGrid size={15} />
          All Trackers
        </button>
        {trackers.map((t) => (
          <button
            key={t.key}
            onClick={() => handleTrackerClick(t.key)}
            className={clsx('sidebar-item w-full justify-between', selectedTracker === t.key && 'active')}
          >
            <span className="flex items-center gap-2">
              {TRACKER_ICONS[t.key] ?? <FolderOpen size={15} />}
              <span className="truncate">{t.label}</span>
            </span>
            {t.total > 0 && (
              <span className="text-[10px] font-medium px-1.5 py-0.5 rounded-full"
                style={{ background: 'var(--border)', color: 'var(--text-tertiary)' }}>
                {t.pending}
              </span>
            )}
          </button>
        ))}
      </div>

      {/* Footer */}
      <div className="px-3 py-3 flex items-center justify-between" style={{ borderTop: '1px solid var(--border)' }}>
        <button
          onClick={fetchTrackers}
          className={clsx('btn-ghost p-1.5 rounded-apple-sm', loading && 'animate-spin')}
          title="Refresh"
        >
          <RefreshCw size={14} />
        </button>
        <button onClick={toggleDarkMode} className="btn-ghost p-1.5 rounded-apple-sm" title="Toggle dark mode">
          {darkMode ? <Sun size={14} /> : <Moon size={14} />}
        </button>
      </div>
    </motion.aside>
  )
}
