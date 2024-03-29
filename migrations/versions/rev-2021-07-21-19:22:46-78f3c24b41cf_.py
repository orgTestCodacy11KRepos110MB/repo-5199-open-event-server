"""empty message

Revision ID: 78f3c24b41cf
Revises: ab0e4baaabab
Create Date: 2021-07-21 19:22:46.736726

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '78f3c24b41cf'
down_revision = 'ab0e4baaabab'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('is_announced', sa.Boolean(), server_default='False', nullable=False))
    op.add_column('events_version', sa.Column('is_announced', sa.Boolean(), server_default='False', autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'is_announced')
    op.drop_column('events', 'is_announced')
    # ### end Alembic commands ###
