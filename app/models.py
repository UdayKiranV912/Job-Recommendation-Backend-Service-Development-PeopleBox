from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    skills = db.Column(db.ARRAY(db.String), nullable=False)
    experience_level = db.Column(db.String(50))
    desired_roles = db.Column(db.ARRAY(db.String))
    locations = db.Column(db.ARRAY(db.String))
    job_type = db.Column(db.String(50))

class JobPosting(db.Model):
    __tablename__ = 'job_postings'
    
    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255))
    required_skills = db.Column(db.ARRAY(db.String), nullable=False)
    location = db.Column(db.String(255))
    job_type = db.Column(db.String(50))
    experience_level = db.Column(db.String(50))
