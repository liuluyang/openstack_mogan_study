#coding:utf8
"""'users-change'

Revision ID: 99405619eeea
Revises: 1dbe5f540fc8
Create Date: 2017-12-15 14:45:06.401000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99405619eeea'
down_revision = '1dbe5f540fc8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('roles', sa.Column('description', sa.String(length=255), nullable=True, default='None'))
    #op.alter_column('roles', sa.Column('desc'))
    #desc是mysql的保留字 所以不能作为column
    #pass


def downgrade():
    #op.drop_column('roles', 'desc')  #success
    pass
