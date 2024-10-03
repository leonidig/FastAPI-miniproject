from pydantic import BaseModel, HttpUrl, Field


class ParseRequest(BaseModel):
    url: HttpUrl = Field(...)