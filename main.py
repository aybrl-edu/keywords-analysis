import json
import time

from flask import Flask, jsonify
from flask_cors import CORS
from worker import consume_kafka
from extract import extract_keywords_data


app = Flask(__name__)
CORS(app)


@app.route('/api/v1/kafka/keywords', methods=['GET'])
def get_keywords_data_kafka():
    start_time = time.time()
    try:
        data = consume_kafka('seo_keywords')

        print("--- execution time for kafka retrieval is %s seconds ---" % (time.time() - start_time))

        return jsonify({"data": json.dumps(data)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/api/v1/json/keywords', methods=['GET'])
def get_keywords_data_json():
    start_time = time.time()
    try:
        f = open('data/kw_data.json')
        data = json.load(f)

        print(len(data['kw_data']))
        print("--- execution time for json retrieval is %s seconds ---" % (time.time() - start_time))

        return jsonify(data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/api/v1/extraction', methods=['GET'])
def start_extraction():
    #extract_keywords_data()
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True)
