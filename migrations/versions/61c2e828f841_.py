"""empty message

Revision ID: 61c2e828f841
Revises: e974427b23e9
Create Date: 2020-08-16 20:35:37.615392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61c2e828f841'
down_revision = 'e974427b23e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('release_date', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('actors')
    # ### end Alembic commands ###