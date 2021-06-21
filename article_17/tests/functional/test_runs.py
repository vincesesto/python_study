"""
This file (test_runs.py) contains the functional tests for the app.py file.
"""
from app import app

def test_get_add_run_page():
    """
    GIVEN a Flask application
    WHEN the '/add_run' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/add_run')
        assert response.status_code == 200
        assert b'Flasking App' in response.data
        assert b'Add a Run' in response.data
        assert b'Type of Run' in response.data
        assert b'Number of Kilometres' in response.data
        assert b'Comments' in response.data


def test_post_add_run_page():
    """
    GIVEN a Flask application
    WHEN the '/add_run' page is posted to (POST)
    THEN check that the user is redirected to the '/runs' page
    """
    with app.test_client() as client:
        response = client.post('/add_run',
                               data={'type_of_run': 'Easy',
                                     'number_of_kilometres': '5',
                                     'comments': 'Easy recovery run'},
                               follow_redirects=True)
        assert response.status_code == 200
        assert b'List of Runs' in response.data
        assert b'Type Of Run' in response.data
        assert b'Number of Kilometres' in response.data
        assert b'Comments' in response.data
        assert b'Easy' in response.data
        assert b'5' in response.data
        assert b'Easy recovery run' in response.data