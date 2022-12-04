from typing import Optional, List
from pydantic import BaseModel, Field


class PieceSchema(BaseModel):
    title: str = Field(...)
    composer: str = Field(...)
    genre: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Moonlight Sonata",
                "composer": "Beethoven, Ludwig van",
                "genre": ["Classical", "Piano"],
            }
        }


class PieceUpdateModel(BaseModel):
    title: Optional[str] = Field(...)
    composer: Optional[str] = Field(...)
    genre: Optional[List[str]] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Moonlight Sonata",
                "composer": "Beethoven, Ludwig van",
                "genre": ["Classical", "Piano"],
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
