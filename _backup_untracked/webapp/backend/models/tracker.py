from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class ItemStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TrackerItem(BaseModel):
    id: str
    tracker: str          # e.g. "bugs", "boss_requests"
    tracker_label: str    # e.g. "Bug Tracker"
    section: Optional[str] = None
    text: str
    status: ItemStatus
    raw_line: str
    line_number: int
    tags: List[str] = []
    priority: Optional[str] = None


class TrackerFile(BaseModel):
    key: str              # config key, e.g. "bugs_master"
    label: str            # display name
    path: str             # relative path
    items: List[TrackerItem]
    total: int
    pending: int
    in_progress: int
    done: int


class SearchResult(BaseModel):
    item: TrackerItem
    score: float
    matches: List[str] = []


class FileNode(BaseModel):
    name: str
    path: str
    type: str             # "file" | "directory"
    size: Optional[int] = None
    children: Optional[List["FileNode"]] = None


FileNode.model_rebuild()


class UpdateItemRequest(BaseModel):
    status: Optional[ItemStatus] = None
    text: Optional[str] = None
