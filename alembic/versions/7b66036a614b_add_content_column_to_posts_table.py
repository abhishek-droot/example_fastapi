"""add Content Column to posts table

Revision ID: 7b66036a614b
Revises: 4a9f06820dc1
Create Date: 2022-11-21 12:33:17.153619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b66036a614b'
down_revision = '4a9f06820dc1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_Column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
