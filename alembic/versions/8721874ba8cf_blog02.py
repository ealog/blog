"""blog02

Revision ID: 8721874ba8cf
Revises: dc09cbe3d9ae
Create Date: 2021-01-10 20:33:36.852340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8721874ba8cf'
down_revision = 'dc09cbe3d9ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True, comment='分类名称'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='所属用户'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_category_user_id'), 'category', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_category_user_id'), table_name='category')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###