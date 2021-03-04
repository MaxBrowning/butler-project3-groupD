from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
from sqlalchemy import create_engine
from config import db_pass

def get_db_data():
    # Connect to database
    connection_string = f"postgres:{db_pass}@localhost:5432/Properties"
    engine = create_engine(f'postgresql://{connection_string}')
    print(engine.table_names())
    # Query data
    sql_query = pd.read_sql_table('property', f'postgresql://{connection_string}')

    # Return data in json format
    return sql_query.to_dict("records")