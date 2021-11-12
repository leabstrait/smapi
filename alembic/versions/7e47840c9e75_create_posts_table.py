"""create posts table

Revision ID: 7e47840c9e75
Revises:
Create Date: 2021-11-12 10:36:49.907040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e47840c9e75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column('id', sa.Integer, nullable=False, primary_key=True, unique=True),
        sa.Column('title', sa.String, nullable=False)
    ),
    pass


def downgrade():
    op.drop_table("posts")
    pass
