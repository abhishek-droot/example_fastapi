"""create Post table

Revision ID: 4a9f06820dc1
Revises: 
Create Date: 2022-11-21 12:21:32.920673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a9f06820dc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(), nullable=False,primary_key=True)
    , sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
