from pydantic import BaseModel


class DashboardStats(BaseModel):
    teams: int
    projects: int
    tasks: int
    completed_tasks: int
    pending_tasks: int
    health: int