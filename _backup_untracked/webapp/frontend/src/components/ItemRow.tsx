import { memo, useState, useRef, useCallback } from 'react'
import { motion } from 'framer-motion'
import { Check, Clock, Minus, Tag, ChevronRight } from 'lucide-react'
import { useStore } from '../stores/useStore'
import type { TrackerItem, ItemStatus } from '../types'
import clsx from 'clsx'

const STATUS_ICONS: Record<ItemStatus, React.ReactNode> = {
  pending: <Clock size={13} />,
  in_progress: <Minus size={13} />,
  done: <Check size={13} strokeWidth={3} />,
}

// Single tap: pending ↔ done (most common mobile action)
// Long press: cycle through all 3 states
const STATUS_TOGGLE: Record<ItemStatus, ItemStatus> = {
  pending: 'done',
  in_progress: 'done',
  done: 'pending',
}

const STATUS_CYCLE: Record<ItemStatus, ItemStatus> = {
  pending: 'in_progress',
  in_progress: 'done',
  done: 'pending',
}

interface Props {
  item: TrackerItem
  showTracker?: boolean
  compact?: boolean
}

export const ItemRow = memo(function ItemRow({ item, showTracker = false, compact = false }: Props) {
  const { updateItemStatus } = useStore()
  const [hovering, setHovering] = useState(false)
  const [pressing, setPressing] = useState(false)
  const longPressTimer = useRef<ReturnType<typeof setTimeout> | null>(null)
  const didLongPress = useRef(false)

  // Short tap: toggle done/pending
  const handleTap = useCallback((e: React.MouseEvent | React.TouchEvent) => {
    e.stopPropagation()
    if (didLongPress.current) {
      didLongPress.current = false
      return
    }
    updateItemStatus(item.tracker, item.id, STATUS_TOGGLE[item.status])
  }, [item.tracker, item.id, item.status, updateItemStatus])

  // Long press: cycle through all 3 states
  const handleTouchStart = useCallback((e: React.TouchEvent) => {
    e.stopPropagation()
    didLongPress.current = false
    setPressing(true)
    longPressTimer.current = setTimeout(() => {
      didLongPress.current = true
      setPressing(false)
      updateItemStatus(item.tracker, item.id, STATUS_CYCLE[item.status])
    }, 500)
  }, [item.tracker, item.id, item.status, updateItemStatus])

  const handleTouchEnd = useCallback(() => {
    if (longPressTimer.current) {
      clearTimeout(longPressTimer.current)
      longPressTimer.current = null
    }
    setPressing(false)
  }, [])

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -4 }}
      onMouseEnter={() => setHovering(true)}
      onMouseLeave={() => setHovering(false)}
      className={clsx(
        'flex items-start gap-3 px-4 rounded-apple-sm transition-all duration-150 cursor-default group',
        compact ? 'py-2' : 'py-3',
        hovering && 'bg-surface'
      )}
    >
      {/* Status toggle — larger on mobile for touch */}
      <button
        onClick={handleTap}
        onTouchStart={handleTouchStart}
        onTouchEnd={handleTouchEnd}
        onTouchCancel={handleTouchEnd}
        className={clsx(
          'status-toggle-btn flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center transition-all duration-150 mt-0.5',
          'border-2 touch-target',
          item.status === 'done' && 'bg-green-500 border-green-500 text-white',
          item.status === 'in_progress' && 'border-blue-500 text-blue-500 bg-blue-500/10',
          item.status === 'pending' && 'border-apple-gray-300 dark:border-apple-gray-600 text-tertiary',
          pressing && 'scale-125',
          !pressing && 'hover:scale-110 active:scale-95'
        )}
        title={`${item.status === 'done' ? 'Mark incomplete' : 'Mark complete'} · Long-press to cycle`}
        aria-label={`Status: ${item.status}. Tap to ${item.status === 'done' ? 'mark incomplete' : 'mark complete'}`}
      >
        {STATUS_ICONS[item.status]}
      </button>

      {/* Content */}
      <div className="flex-1 min-w-0">
        <div className="flex items-start gap-2">
          <span
            className={clsx(
              'text-sm leading-snug flex-1',
              item.status === 'done' ? 'line-through text-tertiary' : 'text-primary'
            )}
          >
            {item.text}
          </span>
          {item.priority && (
            <span className="flex-shrink-0 text-[10px] font-semibold px-1.5 py-0.5 rounded-full bg-red-100 dark:bg-red-900/30 text-red-600 dark:text-red-400">
              {item.priority}
            </span>
          )}
        </div>

        {/* Meta row */}
        {!compact && (
          <div className="flex items-center gap-2 mt-1 flex-wrap">
            {showTracker && (
              <span className="text-[11px] text-tertiary flex items-center gap-1">
                <ChevronRight size={10} />
                {item.tracker_label}
              </span>
            )}
            {item.section && (
              <span className="text-[11px] text-tertiary">{item.section}</span>
            )}
            {item.tags.map((tag) => (
              <span key={tag} className="text-[10px] flex items-center gap-0.5 text-blue-500">
                <Tag size={9} />
                {tag}
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Status badge — hidden on very small screens to save space */}
      <span className={clsx('status-badge flex-shrink-0 mt-0.5 hidden sm:inline-flex', `status-${item.status}`)}>
        {item.status === 'in_progress' ? 'In Progress' : item.status.charAt(0).toUpperCase() + item.status.slice(1)}
      </span>
    </motion.div>
  )
})
