"""init

Revision ID: 5b1f2cf998db
Revises: 
Create Date: 2022-07-29 16:22:14.433814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1f2cf998db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vessels',
    sa.Column('code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_vessels_code'), 'vessels', ['code'], unique=True)
    op.create_table('equipments',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('vessel_code', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['vessel_code'], ['vessels.code'], ),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_equipments_code'), 'equipments', ['code'], unique=True)
    op.create_index(op.f('ix_equipments_name'), 'equipments', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_equipments_name'), table_name='equipments')
    op.drop_index(op.f('ix_equipments_code'), table_name='equipments')
    op.drop_table('equipments')
    op.drop_index(op.f('ix_vessels_code'), table_name='vessels')
    op.drop_table('vessels')
    # ### end Alembic commands ###
