import unittest
from app import create_app, db
from app.models import Agent, InteractionType, AgentBehavior

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_agent_creation(self):
        agent = Agent(name='John Doe')
        db.session.add(agent)
        db.session.commit()
        self.assertEqual(Agent.query.count(), 1)

    def test_interaction_type_creation(self):
        interaction_type = InteractionType(name='Email')
        db.session.add(interaction_type)
        db.session.commit()
        self.assertEqual(InteractionType.query.count(), 1)

    def test_agent_behavior_creation(self):
        agent = Agent(name='John Doe')
        interaction_type = InteractionType(name='Email')
        db.session.add(agent)
        db.session.add(interaction_type)
        db.session.commit()

        behavior = AgentBehavior(agent_id=agent.id, interaction_type_id=interaction_type.id, qa_score=95.0)
        db.session.add(behavior)
        db.session.commit()

        self.assertEqual(AgentBehavior.query.count(), 1)

if __name__ == '__main__':
    unittest.main()