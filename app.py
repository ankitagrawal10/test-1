import requests

def fetch_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website content: \n{response.text[:500]}...")  # Print the first 500 characters of the page
        else:
            print(f"Error: Unable to fetch {url} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter a URL to fetch: ")
    fetch_website(url)


