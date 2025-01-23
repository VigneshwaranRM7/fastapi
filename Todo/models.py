from pydantic import BaseModel,Field
from typing import Optional
from .database import get_next_sequence

class User(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: get_next_sequence('user_id'))
    title: str
    # description: str
    status: bool

    