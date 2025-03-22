import pytest
from app import fetch_website_content

def test_fetch_valid_url():
    url = "https://www.example.com"
    content = fetch_website_content(url)
    assert "Example Domain" in content  # Example.com always contains this text

def test_fetch_invalid_url():
    url = "https://invalid-url-123.com"
    content = fetch_website_content(url)
    assert "Error" in content  # Should return an error message

if __name__ == "__main__":
    pytest.main()
