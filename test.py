import pytest
from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Simple Python Web App" in response.data

def test_fetch_website():
    client = app.test_client()
    response = client.post('/fetch', data={'url': 'https://example.com'})
    assert response.status_code == 200
