export type ItemStatus = 'pending' | 'in_progress' | 'done'

export interface TrackerItem {
  id: string
  tracker: string
  tracker_label: string
  section: string | null
  text: string
  status: ItemStatus
  raw_line: string
  line_number: number
  tags: string[]
  priority: string | null
}

export interface TrackerFile {
  key: string
  label: string
  path: string
  items: TrackerItem[]
  total: number
  pending: number
  in_progress: number
  done: number
}

export interface SearchResult {
  item: TrackerItem
  score: number
  matches: string[]
}

export type ViewMode = 'list' | 'board' | 'kanban' | 'search'

export interface FilterState {
  status: ItemStatus | 'all'
  tracker: string | 'all'
  query: string
}
