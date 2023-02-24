import pytest
from flask import g, session

from newspress.database import get_database

def test_register(client, app):
    ''' Test the user register process '''
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register',
        data={
            'username': 'duketester', 'phone': '073458922',
            'email': 'duketest@gmail.com', 'fullname': 'duke tester',
            'password': 'duketest2030',
            },
    )
    assert response.headers['Location'] == '/auth/login'
    with app.app_context():
        assert get_database().execute(
            ''' SELECT * FROM user WHERE username = 'duketester' ''',
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'phone', 'email', 'fullname', 'password'),
   (('', '073458922', 'duketest@gmail.com',  'duke tester',
    'duketest2030',  b'Username is required'),
    ('duketester', '073458922', 'duketest@gmail.com',
    'duke tester', '', b'Password is required'),
    ('duketester', '', 'duketest@gmail.com',  'duke tester',
    'duketest2030', b'Phone number is required'),
    ('duketester', '073458922', '',  'duke tester',
    'duketest2030', b'Email is required'),
    ('duketester', '073458922', 'duketest@gmail.com',  '',
    'duketest2030', b'Full Name is required'),
    ))
def test_register_validate_input(client, username, phone, email, fullname, password, message):
    response = client.post(
        '/auth/register',
        data={
            'username': username, 'phone': phone,
            'email': email, 'fullname': fullname,
            'password': password,
            }
    )
    assert message in response.data
