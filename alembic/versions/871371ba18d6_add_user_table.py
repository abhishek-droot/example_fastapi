"""add User Table

Revision ID: 871371ba18d6
Revises: 7b66036a614b
Create Date: 2022-11-21 12:40:40.615589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871371ba18d6'
down_revision = '7b66036a614b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(), nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')          
                              )
    pass


def downgrade():
    op.drop_table('users')
    pass
