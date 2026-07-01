from pydantic import BaseModel


class TeamCreate(BaseModel):
    name: str
    description: str | None = None


class TeamResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    owner_id: int

    class Config:
        from_attributes = True