"""admin mixin for contracts

Revision ID: 7ef5e343424f
Revises: 7415503b7089
Create Date: 2024-05-08 15:19:03.509277

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "7ef5e343424f"
down_revision: Union[str, None] = "7415503b7089"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("contracts", sa.Column("created_by", sa.Uuid(), nullable=False))
    op.add_column("contracts", sa.Column("updated_by", sa.Uuid(), nullable=True))
    op.add_column("contracts", sa.Column("deleted_by", sa.Uuid(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("contracts", "deleted_by")
    op.drop_column("contracts", "updated_by")
    op.drop_column("contracts", "created_by")
    # ### end Alembic commands ###
