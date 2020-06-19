from flask import Flask, jsonify, request
from flask_cors import CORS

from search import search

import time

app = Flask(__name__)
CORS(app)

import sys

sys.path.append('')


@app.route('/', methods=['GET'])
def index():
    return jsonify('hahaha')


@app.route('/search', methods=['GET', 'POST'])
def books():
    text = request.args.get('q', '')
    if text != '':
        start_time = time.time()
        result = search(text)
        r = result['hits']['hits']
        end_time = time.time()
        return jsonify({'result': r, 'runtime':endtime-starttime})
    else:
        return jsonify(['none',0.0])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7777, threaded=True)
