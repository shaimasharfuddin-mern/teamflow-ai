from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    team_id = Column(
        Integer,
        ForeignKey("teams.id"),
        nullable=False,
    )

    team = relationship(
        "Team",
        back_populates="projects",
    )

    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
    )