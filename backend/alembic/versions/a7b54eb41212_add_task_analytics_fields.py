"""add task analytics fields

Revision ID: a7b54eb41212
Revises: d3a6425eb12e
Create Date: 2026-07-01
"""

from alembic import op
import sqlalchemy as sa


revision = 'a7b54eb41212'
down_revision = 'd3a6425eb12e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Only add columns if they don't exist already (safe dev fix)
    conn = op.get_bind()

    inspector = sa.inspect(conn)
    columns = [c["name"] for c in inspector.get_columns("tasks")]

    if "due_date" not in columns:
        op.add_column("tasks", sa.Column("due_date", sa.DateTime(), nullable=True))

    if "created_at" not in columns:
        op.add_column("tasks", sa.Column("created_at", sa.DateTime(), nullable=True))

    if "updated_at" not in columns:
        op.add_column("tasks", sa.Column("updated_at", sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column("tasks", "due_date")
    op.drop_column("tasks", "created_at")
    op.drop_column("tasks", "updated_at")