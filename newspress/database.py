''' Create the database '''
import sqlite3
import click
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

# Initialize the database
def init_db():
    db = get_database()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    # Clear the existing data and create new tables
    init_db()
    click.echo('Database initialized successfully!')

def init_app(app):
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_db_command)