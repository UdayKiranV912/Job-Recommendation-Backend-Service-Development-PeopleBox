def match_score(user, job_posting):
    skill_match = len(set(user['skills']) & set(job_posting['required_skills'])) / len(job_posting['required_skills'])
    experience_match = user['experience_level'] == job_posting['experience_level']
    location_match = any(loc in job_posting['location'] for loc in user['preferences']['locations'])
    job_type_match = job_posting['job_type'] == user['preferences']['job_type']
    score = (skill_match * 0.5) + (experience_match * 0.2) + (location_match * 0.15) + (job_type_match * 0.15)
    return score

def get_recommendations(user_profile, job_postings):
    recommended_jobs = []
    
    for job in job_postings:
        score = match_score(user_profile, job)
        if score > 0:  
            recommended_jobs.append({**job, 'match_score': score})
    
    recommended_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    
    return recommended_jobs
