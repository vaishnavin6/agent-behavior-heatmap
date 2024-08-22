from datetime import datetime
from app import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class InteractionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class AgentBehavior(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
    interaction_type_id = db.Column(db.Integer, db.ForeignKey('interaction_type.id'), nullable=False)
    qa_score = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    agent = db.relationship('Agent', backref='agent_behaviors')
    interaction_type = db.relationship('InteractionType', backref='agent_behaviors')