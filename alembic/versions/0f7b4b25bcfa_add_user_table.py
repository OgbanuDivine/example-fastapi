"""add user table

Revision ID: 0f7b4b25bcfa
Revises: 62f069c37ae3
Create Date: 2026-02-12 09:06:41.171957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f7b4b25bcfa'
down_revision: Union[str, Sequence[str], None] = '62f069c37ae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email'))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('users')
    """Downgrade schema."""
    pass
