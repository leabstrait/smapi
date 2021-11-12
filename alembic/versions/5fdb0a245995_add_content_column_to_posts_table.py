"""add content column to posts table

Revision ID: 5fdb0a245995
Revises: 7e47840c9e75
Create Date: 2021-11-12 11:32:23.338427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fdb0a245995'
down_revision = '7e47840c9e75'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column("posts", 'content')
    pass
