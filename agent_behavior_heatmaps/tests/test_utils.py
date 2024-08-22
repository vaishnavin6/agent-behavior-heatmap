import unittest
import pandas as pd
from app.utils.data_processing import load_data, create_pivot_table, populate_database
from app import create_app, db
from app.models import Agent, InteractionType, AgentBehavior

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Mock data
        self.data = {
            'AgentName': ['John Doe', 'Jane Doe', 'John Doe'],
            'InteractionType': ['Email', 'Chat', 'Phone'],
            'QAScore': [90, 85, 95],
            'Date': ['2024-08-19', '2024-08-20', '2024-08-21']
        }
        self.df = pd.DataFrame(self.data)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_load_data(self):
        # Load data directly from the dataframe
        df = load_data(self.df)
        self.assertEqual(df.shape[0], 3)
        self.assertIn('Date', df.columns)

    def test_populate_database(self):
        # Populate database with mock data
        populate_database(self.df)
        self.assertEqual(Agent.query.count(), 2)  # Two unique agents
        self.assertEqual(InteractionType.query.count(), 3)  # Three unique interaction types
        self.assertEqual(AgentBehavior.query.count(), 3)  # Three behaviors

    def test_create_pivot_table(self):
        pivot_table = create_pivot_table(self.df)
        self.assertEqual(pivot_table.shape, (2, 3))  # 2 agents and 3 interaction types

if __name__ == '__main__':
    unittest.main()