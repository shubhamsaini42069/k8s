from flask import Flask, jsonify, request, render_template
import requests
import os

# Backend URL (default to localhost if not set)
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5000')

app = Flask(__name__)
port = int(os.environ.get('PORT', 9000))

@app.route('/')
def index():
    try:
        # Call backend API to get data
        response = requests.get(f'{BACKEND_URL}/api/get')
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("Error connecting to backend:", e)
        data = {'names': ['Error fetching data']}

    # Load environment variables
    env = dict(os.environ)

    # Render the template with data and env
    return render_template('index.html', env=env, data=data['names'])

if __name__ == '__main__':
    app.run(debug=True, port=port, host='0.0.0.0')
