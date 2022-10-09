"""empty message

Revision ID: ba4e4a452241
Revises: dccc6354e216
Create Date: 2022-10-08 13:28:53.180910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba4e4a452241'
down_revision = 'dccc6354e216'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deals', sa.Column('slug', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('deals', 'slug')
    # ### end Alembic commands ###
