"""empty message

Revision ID: 1e069a1b5939
Revises: b4a245fea15f
Create Date: 2021-03-10 19:23:21.681112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e069a1b5939'
down_revision = 'b4a245fea15f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=True),
    sa.Column('precio', sa.String(length=6), nullable=True),
    sa.Column('peso', sa.String(length=7), nullable=True),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('producto')
    # ### end Alembic commands ###
