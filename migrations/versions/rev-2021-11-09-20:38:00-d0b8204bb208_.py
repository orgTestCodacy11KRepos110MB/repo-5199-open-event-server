"""empty message

Revision ID: d0b8204bb208
Revises: b3cf88a46150
Create Date: 2021-11-09 20:38:00.667031

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'd0b8204bb208'
down_revision = 'b3cf88a46150'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('stripe_session_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'stripe_session_id')
    # ### end Alembic commands ###
