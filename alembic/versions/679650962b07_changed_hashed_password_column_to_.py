"""changed hashed_password column to password

Revision ID: 679650962b07
Revises: fe0c6b53921e
Create Date: 2024-09-14 11:31:19.159645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '679650962b07'
down_revision: Union[str, None] = 'fe0c6b53921e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('password', sa.String(), nullable=False))
    op.drop_column('doctors', 'hashed_password')
    op.add_column('patients', sa.Column('password', sa.String(), nullable=False))
    op.drop_column('patients', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('patients', 'password')
    op.add_column('doctors', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('doctors', 'password')
    # ### end Alembic commands ###
