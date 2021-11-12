"""add foreign-key to posts table

Revision ID: 315e282938c1
Revises: 332ffb5756f2
Create Date: 2021-11-12 12:26:49.826782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315e282938c1'
down_revision = '332ffb5756f2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column('owner_id', sa.Integer, nullable=False)
    )
    op.create_foreign_key(
        constraint_name='posts_users_fkey',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint(constraint_name='posts_users_fkey', table_name="posts")
    op.drop_column(table_name="posts", column_name="owner_id")
    pass
