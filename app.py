from flask import Flask, render_template_string, request
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return '''
        <h1>Simple Python Web App</h1>
        <form action="/fetch" method="post">
            <label for="url">Enter a URL:</label>
            <input type="text" id="url" name="url" required>
            <input type="submit" value="Fetch">
        </form>
    '''

# Define a route to handle the form submission
@app.route('/fetch', methods=['POST'])
def fetch_website():
    url = request.form['url']
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text[:500]  # Show the first 500 characters of the website
            return f'''
                <h1>Website Content</h1>
                <p><strong>Content from {url}:</strong></p>
                <pre>{content}</pre>
                <a href="/">Go back</a>
            '''
        else:
            return f"Error: Unable to fetch {url} (Status Code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


