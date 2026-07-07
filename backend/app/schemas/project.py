from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str | None = None


class ProjectCreate(ProjectBase):
    team_id: int


class ProjectUpdate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int
    team_id: int

    class Config:
        from_attributes = True