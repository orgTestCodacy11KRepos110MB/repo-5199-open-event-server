"""empty message

Revision ID: bf42a2f36c31
Revises: 5b53dc97de89
Create Date: 2021-10-22 23:42:31.715908

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'bf42a2f36c31'
down_revision = '5b53dc97de89'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tax', sa.Column('contact_name', sa.String(), nullable=True))
    op.add_column('tax', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('tax', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tax', 'email')
    op.drop_column('tax', 'phone')
    op.drop_column('tax', 'contact_name')
    # ### end Alembic commands ###
