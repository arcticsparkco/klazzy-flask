"""empty message

Revision ID: 10b968c90115
Revises: 9846a17db41d
Create Date: 2022-09-27 17:07:56.643421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b968c90115'
down_revision = '9846a17db41d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('valid_until', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('places',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('places')
    op.drop_table('deals')
    # ### end Alembic commands ###
