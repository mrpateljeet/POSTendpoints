# In your app.py (or main file)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tweets', methods=['POST'])
def create_tweet():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400

    

    return jsonify({'message': 'Tweet created successfully'}), 201
