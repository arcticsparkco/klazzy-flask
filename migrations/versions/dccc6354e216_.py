"""empty message

Revision ID: dccc6354e216
Revises: bfe89635747c
Create Date: 2022-10-02 11:26:28.825674

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dccc6354e216'
down_revision = 'bfe89635747c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'deals', 'users', ['owner_id'], ['id'])
    op.drop_column('deals', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deals', sa.Column('author_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'deals', type_='foreignkey')
    # ### end Alembic commands ###
