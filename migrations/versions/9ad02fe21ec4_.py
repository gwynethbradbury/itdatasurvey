"""empty message

Revision ID: 9ad02fe21ec4
Revises: be2fda7cacff
Create Date: 2018-05-25 14:07:11.088176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad02fe21ec4'
down_revision = 'be2fda7cacff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('webhosting_survey', sa.Column('other_site', sa.String(length=20), nullable=True))
    op.add_column('webhosting_survey', sa.Column('site', sa.Enum('first site', 'Other'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('webhosting_survey', 'site')
    op.drop_column('webhosting_survey', 'other_site')
    # ### end Alembic commands ###