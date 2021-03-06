"""made admin default as False

Revision ID: d66def8b9a1c
Revises: 43a05ed1072f
Create Date: 2020-03-04 00:09:05.199538

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd66def8b9a1c'
down_revision = '43a05ed1072f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=128),
               nullable=False)
    # ### end Alembic commands ###
