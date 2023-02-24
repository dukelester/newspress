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
