# In test/test_app.py

import json
from app import app

def test_create_tweet_success():
    client = app.test_client()
    data = {'text': 'This is a test tweet'}
    
    response = client.post('/tweets', data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == 201
    assert 'message' in response.get_json()
    assert response.get_json()['message'] == 'Tweet created successfully'

def test_create_tweet_failure():
    client = app.test_client()
    data = {}  # This is a bad request as 'text' is missing
    
    response = client.post('/tweets', data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == 400
    assert 'error' in response.get_json()
    assert response.get_json()['error'] == 'Missing text field'
