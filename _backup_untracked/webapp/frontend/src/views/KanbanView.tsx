import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
  DndContext,
  DragOverlay,
  closestCenter,
  PointerSensor,
  useSensor,
  useSensors,
  type DragEndEvent,
  type DragStartEvent,
} from '@dnd-kit/core'
import { SortableContext, useSortable, verticalListSortingStrategy } from '@dnd-kit/sortable'
import { CSS } from '@dnd-kit/utilities'
import { useStore } from '../stores/useStore'
import { ItemRow } from '../components/ItemRow'
import type { TrackerItem, ItemStatus } from '../types'
import clsx from 'clsx'

const COLUMNS: { id: ItemStatus; label: string; color: string }[] = [
  { id: 'pending', label: 'Pending', color: 'text-yellow-500' },
  { id: 'in_progress', label: 'In Progress', color: 'text-blue-500' },
  { id: 'done', label: 'Done', color: 'text-green-500' },
]

function SortableItem({ item }: { item: TrackerItem }) {
  const { attributes, listeners, setNodeRef, transform, transition, isDragging } = useSortable({ id: item.id })
  return (
    <div
      ref={setNodeRef}
      style={{ transform: CSS.Transform.toString(transform), transition, opacity: isDragging ? 0.4 : 1 }}
      {...attributes}
      {...listeners}
    >
      <div className="glass-card mb-2 overflow-hidden">
        <ItemRow item={item} showTracker compact />
      </div>
    </div>
  )
}

export function KanbanView() {
  const { filteredItems, updateItemStatus } = useStore()
  const [activeId, setActiveId] = useState<string | null>(null)
  const items = filteredItems()

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 8 } })
  )

  const byStatus = (status: ItemStatus) => items.filter((i) => i.status === status)
  const activeItem = activeId ? items.find((i) => i.id === activeId) : null

  const handleDragStart = (e: DragStartEvent) => setActiveId(String(e.active.id))

  const handleDragEnd = (e: DragEndEvent) => {
    setActiveId(null)
    const { active, over } = e
    if (!over || active.id === over.id) return

    // Determine target column from over.id (could be column id or item id)
    const targetStatus = COLUMNS.find((c) => c.id === over.id)?.id
      ?? items.find((i) => i.id === over.id)?.status

    if (!targetStatus) return
    const draggedItem = items.find((i) => i.id === active.id)
    if (!draggedItem || draggedItem.status === targetStatus) return
    updateItemStatus(draggedItem.tracker, draggedItem.id, targetStatus)
  }

  return (
    <motion.div
      key="kanban"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="h-full p-4 overflow-x-auto"
    >
      <DndContext sensors={sensors} collisionDetection={closestCenter} onDragStart={handleDragStart} onDragEnd={handleDragEnd}>
        <div className="flex gap-4 h-full min-w-max">
          {COLUMNS.map((col) => {
            const colItems = byStatus(col.id)
            return (
              <div key={col.id} className="w-72 flex flex-col flex-shrink-0">
                {/* Column header */}
                <div className="flex items-center justify-between mb-3 px-1">
                  <div className="flex items-center gap-2">
                    <span className={clsx('text-sm font-semibold', col.color)}>{col.label}</span>
                    <span className="text-xs text-tertiary px-1.5 py-0.5 rounded-full"
                      style={{ background: 'var(--border)' }}>
                      {colItems.length}
                    </span>
                  </div>
                </div>

                {/* Drop zone */}
                <SortableContext items={colItems.map((i) => i.id)} strategy={verticalListSortingStrategy}>
                  <div
                    className="flex-1 rounded-apple p-2 overflow-y-auto min-h-[200px]"
                    style={{ background: 'var(--border)' }}
                    id={col.id}
                  >
                    <AnimatePresence>
                      {colItems.map((item) => (
                        <SortableItem key={item.id} item={item} />
                      ))}
                    </AnimatePresence>
                    {colItems.length === 0 && (
                      <div className="flex items-center justify-center h-20 text-xs text-tertiary">
                        Drop items here
                      </div>
                    )}
                  </div>
                </SortableContext>
              </div>
            )
          })}
        </div>

        <DragOverlay>
          {activeItem && (
            <div className="glass-card shadow-apple-lg rotate-1 scale-105">
              <ItemRow item={activeItem} showTracker compact />
            </div>
          )}
        </DragOverlay>
      </DndContext>
    </motion.div>
  )
}
