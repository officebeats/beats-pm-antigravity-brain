import { motion } from 'framer-motion'
import { Filter } from 'lucide-react'
import { useStore } from '../stores/useStore'
import type { ItemStatus } from '../types'
import clsx from 'clsx'

const STATUS_OPTIONS: { value: ItemStatus | 'all'; label: string }[] = [
  { value: 'all', label: 'All' },
  { value: 'pending', label: 'Pending' },
  { value: 'in_progress', label: 'In Progress' },
  { value: 'done', label: 'Done' },
]

const VIEW_TITLES: Record<string, string> = {
  board: 'Board',
  list: 'List',
  kanban: 'Kanban',
  search: 'Search',
}

export function Header() {
  const { view, filter, setFilter, trackers, selectedTracker } = useStore()

  const title = selectedTracker
    ? trackers.find((t) => t.key === selectedTracker)?.label ?? 'Tracker'
    : VIEW_TITLES[view] ?? 'Brain'

  const totalItems = trackers.reduce((s, t) => s + t.total, 0)
  const pendingItems = trackers.reduce((s, t) => s + t.pending, 0)

  return (
    <motion.header
      initial={{ y: -10, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.25, delay: 0.05 }}
      className="flex items-center justify-between px-3 sm:px-6 py-3 flex-shrink-0"
      style={{ borderBottom: '1px solid var(--border)', background: 'var(--surface)', backdropFilter: 'blur(20px)' }}
    >
      <div className="flex items-center gap-3">
        <h1 className="text-lg font-semibold text-primary">{title}</h1>
        <div className="flex items-center gap-1.5 text-xs text-tertiary">
          <span>{totalItems} items</span>
          <span>·</span>
          <span className="text-yellow-500">{pendingItems} pending</span>
        </div>
      </div>

      {view !== 'search' && (
        <div className="flex items-center gap-2">
          <Filter size={13} className="text-tertiary" />
          <div className="flex items-center gap-1 p-0.5 rounded-apple-sm" style={{ background: 'var(--border)' }}>
            {STATUS_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                onClick={() => setFilter({ status: opt.value })}
                className={clsx(
                  'px-2.5 py-1 rounded-[6px] text-xs font-medium transition-all duration-150',
                  filter.status === opt.value
                    ? 'bg-white dark:bg-apple-gray-700 text-primary shadow-sm'
                    : 'text-secondary hover:text-primary'
                )}
              >
                {opt.label}
              </button>
            ))}
          </div>
        </div>
      )}
    </motion.header>
  )
}
