"""create orders

Revision ID: de2f59c19dc2
Revises: 541c9f96493d
Create Date: 2022-06-15 19:00:26.977330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de2f59c19dc2'
down_revision = '541c9f96493d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL,
            CONSTRAINT fk_orders_custoers
                FOREIGN KEY(customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE orders;
        """
    )
