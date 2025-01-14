"""new attributes education years and first payment due date

Revision ID: d0634d1d8108
Revises: fa0b05ee8ff7
Create Date: 2024-05-15 13:37:04.478862

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "d0634d1d8108"
down_revision: Union[str, None] = "fa0b05ee8ff7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "contract_templates",
        sa.Column("first_payment_due_date", sa.DateTime(timezone=True), nullable=False),
    )
    op.add_column(
        "contract_templates", sa.Column("education_years", sa.String(), nullable=False)
    )
    op.add_column(
        "contracts",
        sa.Column("first_payment_due_date", sa.DateTime(timezone=True), nullable=False),
    )
    op.add_column(
        "contracts", sa.Column("education_years", sa.String(), nullable=False)
    )
    op.add_column(
        "faculty_students_counter",
        sa.Column("education_years", sa.String(), nullable=False),
    )
    op.drop_column("faculty_students_counter", "year")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "faculty_students_counter",
        sa.Column("year", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("faculty_students_counter", "education_years")
    op.drop_column("contracts", "education_years")
    op.drop_column("contracts", "first_payment_due_date")
    op.drop_column("contract_templates", "education_years")
    op.drop_column("contract_templates", "first_payment_due_date")
    # ### end Alembic commands ###
