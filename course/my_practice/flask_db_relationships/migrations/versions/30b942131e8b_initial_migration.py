"""initial migration

Revision ID: 30b942131e8b
Revises: 
Create Date: 2020-05-03 20:05:26.561581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b942131e8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toys')
    op.drop_table('owner')
    op.drop_table('puppies')
    # ### end Alembic commands ###
