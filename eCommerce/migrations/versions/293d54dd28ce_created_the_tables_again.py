"""Created the tables again

Revision ID: 293d54dd28ce
Revises: 
Create Date: 2020-01-23 03:03:58.237563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293d54dd28ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=128), nullable=True),
    sa.Column('category_description', sa.String(length=500), nullable=True),
    sa.Column('category_image', sa.String(length=200), nullable=False),
    sa.Column('category_addedOn', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_category_addedOn'), 'category', ['category_addedOn'], unique=False)
    op.create_index(op.f('ix_category_category_name'), 'category', ['category_name'], unique=True)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=128), nullable=True),
    sa.Column('product_description', sa.String(length=500), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.Column('product_image', sa.String(length=200), nullable=True),
    sa.Column('product_addedOn', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_product_addedOn'), 'product', ['product_addedOn'], unique=False)
    op.create_index(op.f('ix_product_product_name'), 'product', ['product_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_product_addedOn'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_category_category_name'), table_name='category')
    op.drop_index(op.f('ix_category_category_addedOn'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
