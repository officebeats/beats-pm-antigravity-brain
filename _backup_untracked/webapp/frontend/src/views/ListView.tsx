import { useMemo, useRef } from 'react'
import { motion } from 'framer-motion'
import { useVirtualizer } from '@tanstack/react-virtual'
import { useStore } from '../stores/useStore'
import { ItemRow } from '../components/ItemRow'

export function ListView() {
  const { filteredItems, selectedTracker } = useStore()
  const items = filteredItems()
  const parentRef = useRef<HTMLDivElement>(null)

  // Group by section
  const grouped = useMemo(() => {
    const map = new Map<string, typeof items>()
    for (const item of items) {
      const key = item.section ?? 'General'
      if (!map.has(key)) map.set(key, [])
      map.get(key)!.push(item)
    }
    return map
  }, [items])

  // Flatten for virtual scroll: section headers + items
  const rows = useMemo(() => {
    const flat: Array<{ type: 'header'; label: string; count: number } | { type: 'item'; item: typeof items[0] }> = []
    for (const [section, sectionItems] of grouped) {
      flat.push({ type: 'header', label: section, count: sectionItems.length })
      for (const item of sectionItems) {
        flat.push({ type: 'item', item })
      }
    }
    return flat
  }, [grouped])

  const virtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: (i) => (rows[i].type === 'header' ? 36 : 56),
    overscan: 10,
  })

  if (items.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-tertiary">
        <div className="text-4xl mb-3">🎉</div>
        <div className="text-sm font-medium">All clear!</div>
        <div className="text-xs mt-1">No items match the current filter</div>
      </div>
    )
  }

  return (
    <motion.div
      key="list"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="h-full flex flex-col"
    >
      {/* Count bar */}
      <div className="px-6 py-2 flex-shrink-0 text-xs text-tertiary" style={{ borderBottom: '1px solid var(--border)' }}>
        {items.length} item{items.length !== 1 ? 's' : ''}
        {selectedTracker && ' in this tracker'}
      </div>

      {/* Virtual list */}
      <div ref={parentRef} className="flex-1 overflow-y-auto px-2">
        <div style={{ height: virtualizer.getTotalSize(), position: 'relative' }}>
          {virtualizer.getVirtualItems().map((vItem) => {
            const row = rows[vItem.index]
            return (
              <div
                key={vItem.key}
                style={{
                  position: 'absolute',
                  top: vItem.start,
                  left: 0,
                  right: 0,
                  height: vItem.size,
                }}
              >
                {row.type === 'header' ? (
                  <div className="flex items-center gap-2 px-4 py-2">
                    <span className="text-xs font-semibold text-secondary uppercase tracking-wide">{row.label}</span>
                    <span className="text-[10px] text-tertiary">({row.count})</span>
                    <div className="flex-1 h-px" style={{ background: 'var(--border)' }} />
                  </div>
                ) : (
                  <ItemRow item={row.item} showTracker={!selectedTracker} />
                )}
              </div>
            )
          })}
        </div>
      </div>
    </motion.div>
  )
}
