import os
from flask import Flask, request, jsonify
import twss_classifier

app = Flask(__name__)

twss_classifier.load()

@app.route('/classify')
def classify():
	query = request.args.get('q', 0, type=str)
	return jsonify(result = twss_classifier.classify(query))

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)