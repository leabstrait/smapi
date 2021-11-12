"""add last few columns to posts table

Revision ID: 71247e1c191c
Revises: 315e282938c1
Create Date: 2021-11-12 12:34:55.204507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71247e1c191c'
down_revision = '315e282938c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(table_name="posts", column=sa.Column("published", sa.Boolean, nullable=False, server_default='True'))
    op.add_column(table_name="posts", column=sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))
    pass


def downgrade():
    op.drop_column(table_name="posts", column_name="published")
    op.drop_column(table_name="posts", column_name="created_at")
    pass
