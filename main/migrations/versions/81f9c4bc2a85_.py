"""empty message

Revision ID: 81f9c4bc2a85
Revises: 
Create Date: 2021-06-24 19:23:09.377374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81f9c4bc2a85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=25), nullable=False),
    sa.Column('superPower', sa.String(length=30), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('poll_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemons')
    # ### end Alembic commands ###
