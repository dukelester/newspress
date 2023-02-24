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

def test_update_blog_post(client, auth, app):
    ''' Testing updating a blog post '''
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'testing updated'})

    with app.app_context():
        db = get_database()
        post = db.execute(
            'SELECT * FROM blog WHERE id = 1'
        ).fetchone()
        assert post['title'] == 'testing updated'

@pytest.mark.parametrize('path', (
    '/create',
    '1/update',
))

def test_create_update_validate(client, auth, path):
    ''' validate the create and update '''
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required' in response.data

def test_delete(client, auth, app):
    ''' delete a post '''
    auth.login()
    response = client.post('/1/delete')
    assert response.headers['Location'] == '/'

    with app.app_context():
        db = get_database()
        post = db.execute('SELECT * FROM blog WHERE id = 1').fetchone()
        assert post is None