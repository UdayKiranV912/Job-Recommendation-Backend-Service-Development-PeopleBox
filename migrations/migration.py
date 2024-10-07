"""Initial migration for User and JobPosting models"""

from alembic import op
import sqlalchemy as sa

revision = '1234567890'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('skills', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('experience_level', sa.String(length=50), nullable=True),
    sa.Column('desired_roles', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('locations', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('job_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )

    op.create_table('job_postings',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(length=255), nullable=False),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('required_skills', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('job_type', sa.String(length=50), nullable=True),
    sa.Column('experience_level', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('job_id')
    )

def downgrade():
    op.drop_table('job_postings')
    op.drop_table('users')
