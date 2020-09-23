"""added history.msg_read

Revision ID: 79ec557bc4d8
Revises: dda3e9e415ab
Create Date: 2020-09-23 16:52:58.631457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79ec557bc4d8'
down_revision = 'dda3e9e415ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('msg_read', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'msg_read')
    # ### end Alembic commands ###