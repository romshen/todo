"""Add a column

Revision ID: 44a330c15646
Revises: 97667ee937ff
Create Date: 2022-05-31 11:57:32.505089+00:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "44a330c15646"
down_revision = "97667ee937ff"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("account", sa.Column("last_transaction_date", sa.DateTime))


def downgrade():
    op.drop_column("account", "last_transaction_date")
