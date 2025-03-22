import pytest
from app import app  # Import the Flask app from your app.py file

# Set up a test client for Flask
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home page (index route)
def test_home(client):
    """Test the homepage route"""
    response = client.get('/')  # Send a GET request to the home route
    assert response.status_code == 200  # Assert that the response status is 200 (OK)
    assert b"Simple Python Web App" in response.data  # Assert that the home page contains this string

# Test the fetch route (simulating form submission)
def test_fetch_website(client):
    """Test the fetch route with a valid URL"""
    # Simulate submitting a form with a valid URL (you can change this URL to anything)
    data = {'url': 'https://example.com'}
    response = client.post('/fetch', data=data)  # Send a POST request to the /fetch route with form data
    
    # Assert that the response status is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response contains part of the URL entered
    assert b"Content from https://example.com" in response.data
    assert len(response.data) > 0  # Ensure that some content is returned


