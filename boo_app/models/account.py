
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    name: str = Field(...)
