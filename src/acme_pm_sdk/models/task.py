from datetime import datetime
from typing import Optional, List, AsyncIterator

from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False
    project_id: str
    assignee_id: Optional[str] = None
    due_date: Optional[datetime] = None