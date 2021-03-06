"""empty message

Revision ID: 987314ccb842
Revises: fc144b72489f
Create Date: 2019-08-08 20:33:54.875275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987314ccb842'
down_revision = 'fc144b72489f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('project_name', sa.String(length=32), nullable=False),
    sa.Column('simple_desc', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_info')
    # ### end Alembic commands ###
