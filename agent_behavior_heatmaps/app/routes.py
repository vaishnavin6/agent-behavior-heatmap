from flask import Blueprint, render_template, current_app as app
from app.utils.data_processing import load_data, populate_database, create_pivot_table
from app.utils.visualization import generate_heatmap

main = Blueprint('main', __name__)

@main.route('/')
def index():
    df = load_data('data/agent_behavior_data.csv')
    populate_database(df)
    pivot_table = create_pivot_table(df)
    generate_heatmap(pivot_table, 'app/static/img/agent_behavior_heatmap.png')
    return render_template('dashboard.html')