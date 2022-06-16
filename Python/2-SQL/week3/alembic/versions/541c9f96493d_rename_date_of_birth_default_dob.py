"""rename date_of_birth default dob

Revision ID: 541c9f96493d
Revises: e610d521118f
Create Date: 2022-06-15 19:00:15.492957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541c9f96493d'
down_revision = 'e610d521118f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth TO dob;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN dob TO date_of_birth;
        """
    )
