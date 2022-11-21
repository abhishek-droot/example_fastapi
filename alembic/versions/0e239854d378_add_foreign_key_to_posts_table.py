"""add foreign key to posts table

Revision ID: 0e239854d378
Revises: 871371ba18d6
Create Date: 2022-11-21 12:51:08.274764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e239854d378'
down_revision = '871371ba18d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_Column('posts',sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
