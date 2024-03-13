
from pydantic import BaseModel, Field


class ProfileSchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    mbti: str = Field(...)
    enneagram: str = Field(...)
    tritype: float = Field(...)
    socionics: str = Field(...)
    sloan: str = Field(...)
    psyche: str = Field(...)
    image: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id"         : 1,
                "name"       : "A Martinez",
                "description": "Adolph Larrue Martinez III.",
                "mbti"       : "ISFJ",
                "enneagram"  : "9w3",
                "variant"    : "sp/so",
                "tritype"    : 725,
                "socionics"  : "SEE",
                "sloan"      : "RCOEN",
                "psyche"     : "FEVL",
                "image"      : "https://soulverse.boo.world/images/1.png",
            }
        }