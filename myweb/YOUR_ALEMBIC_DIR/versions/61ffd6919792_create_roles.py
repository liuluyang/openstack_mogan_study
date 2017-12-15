"""'create-roles'

Revision ID: 61ffd6919792
Revises: 11b594075656
Create Date: 2017-12-15 10:52:42.048000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ffd6919792'
down_revision = '11b594075656'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False)
    )
    #pass


def downgrade():
    pass
