import { memo } from 'react'
import { motion } from 'framer-motion'
import { Bug, Star, Scale, FolderOpen, Users, Code2, Palette, ArrowRight } from 'lucide-react'
import { useStore } from '../stores/useStore'
import type { TrackerFile } from '../types'
import clsx from 'clsx'

const TRACKER_ICONS: Record<string, React.ReactNode> = {
  bugs_master: <Bug size={18} />,
  boss_requests: <Star size={18} />,
  decision_log: <Scale size={18} />,
  projects_master: <FolderOpen size={18} />,
  delegated_tasks: <Users size={18} />,
  eng_tasks: <Code2 size={18} />,
  ux_tasks: <Palette size={18} />,
}

const TRACKER_COLORS: Record<string, string> = {
  bugs_master: 'from-red-500 to-orange-500',
  boss_requests: 'from-yellow-500 to-amber-500',
  decision_log: 'from-purple-500 to-violet-500',
  projects_master: 'from-blue-500 to-cyan-500',
  delegated_tasks: 'from-green-500 to-emerald-500',
  eng_tasks: 'from-indigo-500 to-blue-500',
  ux_tasks: 'from-pink-500 to-rose-500',
}

interface Props {
  tracker: TrackerFile
  index: number
}

export const TrackerCard = memo(function TrackerCard({ tracker, index }: Props) {
  const { setSelectedTracker, setView } = useStore()
  const gradient = TRACKER_COLORS[tracker.key] ?? 'from-gray-500 to-slate-500'
  const pct = tracker.total > 0 ? Math.round((tracker.done / tracker.total) * 100) : 0

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: index * 0.05, ease: [0.34, 1.56, 0.64, 1] }}
      onClick={() => { setSelectedTracker(tracker.key); setView('list') }}
      className="glass-card-hover p-5 cursor-pointer select-none"
    >
      {/* Icon + title */}
      <div className="flex items-start justify-between mb-4">
        <div className={clsx('w-10 h-10 rounded-apple-sm bg-gradient-to-br flex items-center justify-center text-white', gradient)}>
          {TRACKER_ICONS[tracker.key] ?? <FolderOpen size={18} />}
        </div>
        <ArrowRight size={14} className="text-tertiary mt-1" />
      </div>

      <div className="mb-3">
        <h3 className="text-sm font-semibold text-primary leading-tight">{tracker.label}</h3>
        <p className="text-xs text-tertiary mt-0.5">{tracker.total} items total</p>
      </div>

      {/* Progress bar */}
      <div className="mb-3">
        <div className="flex justify-between text-[10px] text-tertiary mb-1">
          <span>{pct}% complete</span>
          <span>{tracker.done}/{tracker.total}</span>
        </div>
        <div className="h-1.5 rounded-full overflow-hidden" style={{ background: 'var(--border)' }}>
          <motion.div
            initial={{ width: 0 }}
            animate={{ width: `${pct}%` }}
            transition={{ duration: 0.6, delay: index * 0.05 + 0.2, ease: 'easeOut' }}
            className={clsx('h-full rounded-full bg-gradient-to-r', gradient)}
          />
        </div>
      </div>

      {/* Status pills */}
      <div className="flex items-center gap-1.5 flex-wrap">
        {tracker.pending > 0 && (
          <span className="status-badge status-pending">{tracker.pending} pending</span>
        )}
        {tracker.in_progress > 0 && (
          <span className="status-badge status-in_progress">{tracker.in_progress} active</span>
        )}
        {tracker.done > 0 && (
          <span className="status-badge status-done">{tracker.done} done</span>
        )}
        {tracker.total === 0 && (
          <span className="text-[11px] text-tertiary">No items yet</span>
        )}
      </div>
    </motion.div>
  )
})
