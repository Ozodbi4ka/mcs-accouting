"""first

Revision ID: 092e0afa6aee
Revises: 
Create Date: 2024-04-11 15:24:38.107826

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "092e0afa6aee"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contract_templates",
        sa.Column("branch_id", sa.Uuid(), nullable=False),
        sa.Column("degree_program", sa.String(), nullable=False),
        sa.Column("language", sa.String(), nullable=False),
        sa.Column("info", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("html_content", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("start_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expiration_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by", sa.Uuid(), nullable=False),
        sa.Column("updated_by", sa.Uuid(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "branch_id",
            "degree_program",
            "language",
            "is_active",
            name="unique_branch_degree_active_constraint",
        ),
    )
    op.create_index(
        op.f("ix_contract_templates_id"),
        "contract_templates",
        ["id"],
        unique=True,
    )
    op.create_table(
        "faculty_contract_prices",
        sa.Column("faculty_id", sa.Uuid(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("transcriptions", sa.JSON(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by", sa.Uuid(), nullable=False),
        sa.Column("updated_by", sa.Uuid(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_faculty_contract_prices_id"),
        "faculty_contract_prices",
        ["id"],
        unique=True,
    )
    op.create_table(
        "faculty_students_counter",
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("faculty_id", sa.Uuid(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_faculty_students_counter_id"),
        "faculty_students_counter",
        ["id"],
        unique=True,
    )
    op.create_table(
        "payments",
        sa.Column("contract_number", sa.String(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=True),
        sa.Column("passport_number", sa.String(), nullable=False),
        sa.Column("pinfl", sa.String(), nullable=True),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_payments_id"), "payments", ["id"], unique=True)
    op.create_table(
        "contracts",
        sa.Column("student_id", sa.Uuid(), nullable=False),
        sa.Column("template_id", sa.Uuid(), nullable=False),
        sa.Column("html_content", sa.String(), nullable=False),
        sa.Column("number", sa.String(), nullable=False),
        sa.Column("download_counter", sa.Integer(), nullable=False),
        sa.Column("start_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expiration_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_downloaded_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("is_archived", sa.Boolean(), nullable=False),
        sa.Column("file_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["template_id"],
            ["contract_templates.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("number"),
    )
    op.create_index(op.f("ix_contracts_id"), "contracts", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_contracts_id"), table_name="contracts")
    op.drop_table("contracts")
    op.drop_index(op.f("ix_payments_id"), table_name="payments")
    op.drop_table("payments")
    op.drop_index(
        op.f("ix_faculty_students_counter_id"),
        table_name="faculty_students_counter",
    )
    op.drop_table("faculty_students_counter")
    op.drop_index(
        op.f("ix_faculty_contract_prices_id"),
        table_name="faculty_contract_prices",
    )
    op.drop_table("faculty_contract_prices")
    op.drop_index(op.f("ix_contract_templates_id"), table_name="contract_templates")
    op.drop_table("contract_templates")
    # ### end Alembic commands ###
