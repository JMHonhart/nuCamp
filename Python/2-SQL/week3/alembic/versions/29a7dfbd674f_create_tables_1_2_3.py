"""create tables 1 2 3

Revision ID: 29a7dfbd674f
Revises: 3723a8ae1c48
Create Date: 2022-06-15 19:01:05.111052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a7dfbd674f'
down_revision = '3723a8ae1c48'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE table1(id SERIAL PRIMARY KEY);
        CREATE TABLE table2(id SERIAL PRIMARY KEY);
        CREATE TABLE table3(id SERIAL PRIMARY KEY);
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE table3;
        DROP TABLE table2;
        DROP TABLE table1;
        """
    )
