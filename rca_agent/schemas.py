from pydantic import BaseModel


class RCARequest(BaseModel):
    error: str


class RCAResponse(BaseModel):
    result: str
