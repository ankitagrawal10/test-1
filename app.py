import requests

def fetch_website_content(url):
    """Fetches and returns the first 500 characters of a webpage."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text[:500]
        else:
            return f"Error: Unable to fetch {url} (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = input("Enter a URL to fetch content: ")
    content = fetch_website_content(url)
    print("\nWebsite Content Preview:")
    print(content)
