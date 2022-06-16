"""set date_of_birth non-nullable

Revision ID: afd2d69cdf9d
Revises: 15475ef28420
Create Date: 2022-06-15 18:59:42.297894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afd2d69cdf9d'
down_revision = '15475ef28420'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )
