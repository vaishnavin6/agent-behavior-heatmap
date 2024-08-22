import unittest
from app import create_app, db
from flask import url_for

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_route(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Agent Behavior Heatmap', response.data)

if __name__ == '__main__':
    unittest.main()