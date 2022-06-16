"""drop fk_orders_customers

Revision ID: 3723a8ae1c48
Revises: de2f59c19dc2
Create Date: 2022-06-15 19:00:52.698890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3723a8ae1c48'
down_revision = 'de2f59c19dc2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE orders
            DROP CONSTRAINT fk_orders_customers;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE orders
        ADD CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE;
        """
    )
