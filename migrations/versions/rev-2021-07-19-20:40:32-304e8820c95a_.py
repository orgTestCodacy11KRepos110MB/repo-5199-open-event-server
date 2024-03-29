"""empty message

Revision ID: 304e8820c95a
Revises: f0ec7ba33589
Create Date: 2021-07-19 20:40:32.484235

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '304e8820c95a'
down_revision = 'f0ec7ba33589'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('contact_email', sa.String(), nullable=True))
    op.add_column('groups', sa.Column('contact_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groups', 'contact_link')
    op.drop_column('groups', 'contact_email')
    # ### end Alembic commands ###
