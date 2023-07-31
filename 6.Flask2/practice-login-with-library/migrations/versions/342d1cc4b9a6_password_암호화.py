"""password 암호화

Revision ID: 342d1cc4b9a6
Revises: 
Create Date: 2023-07-31 10:38:44.746544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '342d1cc4b9a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=120), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=120), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
