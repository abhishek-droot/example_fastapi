"""add last few columns to posts table

Revision ID: 13ff71e0e796
Revises: 0e239854d378
Create Date: 2022-11-21 12:58:09.186682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13ff71e0e796'
down_revision = '0e239854d378'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
    ),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
