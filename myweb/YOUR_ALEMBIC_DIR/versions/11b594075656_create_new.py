"""'create-new'

Revision ID: 11b594075656
Revises: 
Create Date: 2017-12-15 09:45:26.838000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b594075656'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('age', sa.Integer, nullable=True)
    )
    #pass


def downgrade():
    pass
