"""initial migration

Revision ID: 155d44a61667
Revises: 
Create Date: 2023-04-11 10:24:12.956652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155d44a61667'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=64), nullable=False),
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=64), nullable=False),
    sa.Column('number_building', sa.Integer(), nullable=False),
    sa.Column('number_flat', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resident',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('second_name', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('middle_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adressobject_resident',
    sa.Column('adressobject_id', sa.Integer(), nullable=True),
    sa.Column('resident_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adressobject_id'], ['adress.id'], ),
    sa.ForeignKeyConstraint(['resident_id'], ['resident.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adressobject_resident')
    op.drop_table('resident')
    op.drop_table('adress')
    # ### end Alembic commands ###
