import sqlite3

import pytest
from newspress.database import get_database

def test_get_close_db(app):
    with app.app_context():
        db = get_database()
        assert db is get_database()
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')
    assert 'closed' in str(e.value)