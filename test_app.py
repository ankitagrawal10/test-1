import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Simple Python Web App" in response.data

def test_fetch_website(client):
    response = client.post('/fetch', data={'url': 'http://example.com'})
    assert response.status_code == 200
    assert b"Website Content" in response.data

