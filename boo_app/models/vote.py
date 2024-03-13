
from pydantic import BaseModel, Field


class VoteOptionSchema(BaseModel):

    category_id: str = Field(...)
    name: str = Field(...)


class VoteOptionCategorySchema(BaseModel):

    name: str = Field(...)


class VoteSchema(BaseModel):

    account_id: str = Field(...)
    profile_id: str = Field(...)
    vote_option_id: str = Field(...)

