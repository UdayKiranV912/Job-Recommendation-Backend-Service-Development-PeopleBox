import unittest
from app import app

class TestJobRecommendationAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_recommend_jobs(self):
        user_profile = {
            "name": "John Doe",
            "skills": ["Python", "Django", "REST APIs"],
            "experience_level": "Intermediate",
            "preferences": {
                "desired_roles": ["Backend Developer"],
                "locations": ["Remote"],
                "job_type": "Full-Time"
            }
        }
        response = self.app.post('/recommend', json=user_profile)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

if __name__ == '__main__':
    unittest.main()
