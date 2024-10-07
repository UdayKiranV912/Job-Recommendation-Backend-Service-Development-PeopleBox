CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    skills TEXT[] NOT NULL,
    experience_level VARCHAR(50),
    desired_roles TEXT[],
    locations TEXT[],
    job_type VARCHAR(50)
);
