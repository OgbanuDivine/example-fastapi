"""add foreign-key to posts table

Revision ID: 1b00e262ea7e
Revises: 0f7b4b25bcfa
Create Date: 2026-02-12 09:33:27.131808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b00e262ea7e'
down_revision: Union[str, Sequence[str], None] = '0f7b4b25bcfa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    """Upgrade schema."""
    pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    """Downgrade schema."""
    pass
