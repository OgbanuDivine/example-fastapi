"""add content column to posts table

Revision ID: 62f069c37ae3
Revises: ad3770743a40
Create Date: 2026-02-11 17:40:31.192398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62f069c37ae3'
down_revision: Union[str, Sequence[str], None] = 'ad3770743a40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    """Downgrade schema."""
    pass
