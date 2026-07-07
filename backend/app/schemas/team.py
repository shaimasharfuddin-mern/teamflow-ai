from pydantic import BaseModel


class TeamBase(BaseModel):
    name: str
    description: str | None = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class TeamResponse(TeamBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True