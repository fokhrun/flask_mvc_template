"""initial migration

Revision ID: ac526e2e59cb
Revises: 
Create Date: 2023-11-04 10:59:41.299215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac526e2e59cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_capacity', sa.Enum('two', 'four', 'six', name='tablecapacity'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('reservation_time_slot', sa.Enum('evening', 'night', name='reservationslot'), nullable=False),
    sa.Column('reservation_date', sa.Date(), nullable=False),
    sa.Column('reservation_status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['table_id'], ['tables.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservations')
    op.drop_table('tables')
    # ### end Alembic commands ###