import pandas as pd
from app.models import Agent, InteractionType, AgentBehavior
from app import db

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def populate_database(df):
    for _, row in df.iterrows():
        agent = Agent.query.filter_by(name=row['AgentName']).first()
        if not agent:
            agent = Agent(name=row['AgentName'])
            db.session.add(agent)
            db.session.commit()

        interaction_type = InteractionType.query.filter_by(name=row['InteractionType']).first()
        if not interaction_type:
            interaction_type = InteractionType(name=row['InteractionType'])
            db.session.add(interaction_type)
            db.session.commit()

        behavior = AgentBehavior(
            agent_id=agent.id,
            interaction_type_id=interaction_type.id,
            qa_score=row['QAScore'],
            date=row['Date']
        )
        db.session.add(behavior)

    db.session.commit()

def create_pivot_table(df):
    return df.pivot_table(index='AgentName', columns='InteractionType', values='QAScore', aggfunc='mean')