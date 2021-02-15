"""registered_users.username UNIQUE

Revision ID: 25fc8579e934
Revises: 429d596c43a7
Create Date: 2020-10-27 22:08:49.126951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25fc8579e934'
down_revision = '429d596c43a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'registered_users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'registered_users', type_='unique')
    # ### end Alembic commands ###