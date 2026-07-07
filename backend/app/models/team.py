from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    owner = relationship(
        "User",
        back_populates="teams",
    )

    members = relationship(
        "TeamMember",
        back_populates="team",
        cascade="all, delete-orphan",
    )

    projects = relationship(
        "Project",
        back_populates="team",
        cascade="all, delete-orphan",
    )
    tasks = relationship(
    "Task",
    back_populates="team",
    cascade="all, delete-orphan",
)