import pytest

from newspress.database import get_database

def test_index(client, auth):
    ''' The index page'''
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.parametrize('path', (
    '/2/update',
    '2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404

def test_create_blog(client, auth, app):
    ''' creating new post '''
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={
        'title': 'test blogger', 'body': '',
    })

    with app.app_context():
        db = get_database()
        count = db.execute('SELECT COUNT(id) FROM blog').fetchone()[0]
        assert count == 4
