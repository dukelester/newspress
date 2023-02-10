''' Create the database '''
import sqlite3
from flask import current_app, g

def get_database():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# close the db

def close_database(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
