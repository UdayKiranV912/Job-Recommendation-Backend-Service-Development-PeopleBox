from flask import Flask, request, jsonify
from app.job_matching import get_recommendations
from app.models import JobPosting

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_jobs():
    user_profile = request.json
    
    job_postings = JobPosting.query.all()
    
    recommended_jobs = get_recommendations(user_profile, job_postings)
    return jsonify(recommended_jobs)

if __name__ == '__main__':
    app.run(debug=True)
