"""add user table

Revision ID: 332ffb5756f2
Revises: 5fdb0a245995
Create Date: 2021-11-12 11:52:26.130093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '332ffb5756f2'
down_revision = '5fdb0a245995'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column('id',sa.Integer, nullable=False),
        sa.Column('email',sa.String, nullable=False),
        sa.Column('password',sa.String, nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
