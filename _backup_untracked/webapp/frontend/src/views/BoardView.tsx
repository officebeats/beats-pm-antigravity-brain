import { useStore } from '../stores/useStore'
import { TrackerCard } from '../components/TrackerCard'
import { motion } from 'framer-motion'

export function BoardView() {
  const { trackers, filter } = useStore()

  const visible = trackers.filter((t) => {
    if (filter.status === 'all') return true
    if (filter.status === 'pending') return t.pending > 0
    if (filter.status === 'in_progress') return t.in_progress > 0
    if (filter.status === 'done') return t.done > 0
    return true
  })

  return (
    <motion.div
      key="board"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="p-3 sm:p-6 overflow-y-auto h-full"
    >
      {/* Summary stats */}
      <div className="grid grid-cols-3 gap-3 mb-6">
        {[
          { label: 'Total Items', value: trackers.reduce((s, t) => s + t.total, 0), color: 'text-primary' },
          { label: 'Pending', value: trackers.reduce((s, t) => s + t.pending, 0), color: 'text-yellow-500' },
          { label: 'Done', value: trackers.reduce((s, t) => s + t.done, 0), color: 'text-green-500' },
        ].map((stat) => (
          <div key={stat.label} className="glass-card px-4 py-3 text-center">
            <div className={`text-2xl font-bold ${stat.color}`}>{stat.value}</div>
            <div className="text-xs text-tertiary mt-0.5">{stat.label}</div>
          </div>
        ))}
      </div>

      {/* Tracker grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {visible.map((tracker, i) => (
          <TrackerCard key={tracker.key} tracker={tracker} index={i} />
        ))}
      </div>

      {visible.length === 0 && (
        <div className="flex flex-col items-center justify-center py-20 text-tertiary">
          <div className="text-4xl mb-3">📭</div>
          <div className="text-sm">No trackers match the current filter</div>
        </div>
      )}
    </motion.div>
  )
}
