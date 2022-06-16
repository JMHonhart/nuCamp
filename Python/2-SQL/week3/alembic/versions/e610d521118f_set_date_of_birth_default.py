"""set date_of_birth default

Revision ID: e610d521118f
Revises: afd2d69cdf9d
Create Date: 2022-06-15 18:59:58.281870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e610d521118f'
down_revision = 'afd2d69cdf9d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )
