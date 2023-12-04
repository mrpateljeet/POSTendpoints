# routes.py
from flask import jsonify, request

def configure_routes(app):
    tweet_data = [
        {"id": 1, "text": "Tweet 1"},
        {"id": 2, "text": "Tweet 2"},
        # ... other tweets
    ]

    # ... other routes

    @app.route('/tweets', methods=['POST'])
    def create_tweet():
        try:
            data = request.get_json()
            if 'text' in data:
                new_tweet = {"id": len(tweet_data) + 1, "text": data['text']}
                tweet_data.append(new_tweet)
                return jsonify(new_tweet), 201  # 201 Created status code
            else:
                return jsonify({"error": "Missing 'text' in request body"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
