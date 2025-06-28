"""mi nueva migracion de prueba

Revision ID: 793524f6aecc
Revises: 7616f093bc69
Create Date: 2025-06-28 17:49:10.840548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '793524f6aecc'
down_revision: Union[str, None] = '7616f093bc69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
