from flask import Flask, jsonify
from flask_cors import CORS
import os
import reddit

app = Flask(__name__)
CORS(app)
rclient = reddit.RedditClient()

@app.route('/gigs')
def get_gigs():
	return jsonify(rclient.get_gigs())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
