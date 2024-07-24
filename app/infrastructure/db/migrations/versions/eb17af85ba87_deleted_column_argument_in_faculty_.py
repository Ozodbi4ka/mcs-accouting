"""deleted column argument in faculty contract price

Revision ID: eb17af85ba87
Revises: 4a34425cc126
Create Date: 2024-05-17 12:11:24.108277

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "eb17af85ba87"
down_revision: Union[str, None] = "4a34425cc126"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "faculty_contract_prices_faculty_id_key",
        "faculty_contract_prices",
        type_="unique",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "faculty_contract_prices_faculty_id_key",
        "faculty_contract_prices",
        ["faculty_id"],
    )
    # ### end Alembic commands ###
