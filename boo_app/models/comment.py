
from datetime import datetime

from pydantic import BaseModel, Field


class CommentSchema(BaseModel):

    title: str = Field(...)
    content: str = Field(...)
    profile_id: str = Field(...)
    account_id: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
