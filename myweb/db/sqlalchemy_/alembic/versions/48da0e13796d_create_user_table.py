"""Create user table

Revision ID: 48da0e13796d
Revises: 
Create Date: 2017-05-08 10:13:53.354000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48da0e13796d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False, unique=True),
        sa.Column('email', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
