"""done

Revision ID: 1e1aa275a41a
Revises: 725cc9945016
Create Date: 2025-01-16 13:42:47.449937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e1aa275a41a'
down_revision = '725cc9945016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('term_fee')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('term_fee', sa.FLOAT(), nullable=False))

    # ### end Alembic commands ###
