"""empty message

Revision ID: 679f234bd5f2
Revises: 
Create Date: 2021-03-08 01:46:40.079899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '679f234bd5f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categoria')
    # ### end Alembic commands ###