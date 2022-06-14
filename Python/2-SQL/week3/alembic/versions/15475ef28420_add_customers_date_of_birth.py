"""add customers date_of_birth

Revision ID: 15475ef28420
Revises: 2c81505bc417
Create Date: 2022-06-13 23:01:52.062106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15475ef28420'
down_revision = '2c81505bc417'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
