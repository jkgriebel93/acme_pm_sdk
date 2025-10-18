from typing import Optional, List

from pydantic import BaseModel


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    is_archived: bool = False
