"""create customers

Revision ID: 2c81505bc417
Revises: 
Create Date: 2022-06-13 22:45:32.369654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c81505bc417'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
