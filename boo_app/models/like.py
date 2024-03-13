
from pydantic import BaseModel, Field


class CommentLikeSchema(BaseModel):

    account_id: str = Field(...)
    comment_id: str = Field(...)

