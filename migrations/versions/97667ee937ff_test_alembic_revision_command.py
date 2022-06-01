"""Test alembic revision command

Revision ID: 97667ee937ff
Revises:
Create Date: 2022-05-31 11:41:53.995467+00:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "97667ee937ff"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("description", sa.Unicode(200)),
    )


def downgrade():
    op.drop_table("account")
