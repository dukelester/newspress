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

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False
    def fake_init_db():
        Recorder.called = True
    monkeypatch.setattr('newspress.database.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Database initialized successfully!' in result.output
    assert Recorder.called
