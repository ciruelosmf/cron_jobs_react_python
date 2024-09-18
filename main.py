import sqlite3
import random
import time
import json
from flask import Flask, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/stream": {"origins": "http://localhost:3000"}})

def fetch_all_responses():
    conn = sqlite3.connect(r'C:\Users\p\Documents\estudios\01\projects\react_cron_jobs_backend\articles_kw_data.db')
    cursor = conn.execute('SELECT id, title, creation_date, keyword FROM articles_kw_data')
    responses = [{"id": row[0], "title": row[1], "creation_date": row[2], "keyword": row[3]} for row in cursor]
    conn.close()
    return responses

def get_random_slice():
    responses = fetch_all_responses()
    total_responses = len(responses)
    start = random.randint(0, max(0, total_responses - 6))
    end = min(start + 5, total_responses)
    return responses[start:end]

@app.route("/api/data", methods=['GET'])
def get_responses():
    return jsonify(get_random_slice())

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            # Wait for 10 seconds
            time.sleep(10)
            # Get new data
            data = get_random_slice()
            yield f"data: {json.dumps(data)}\n\n"

    response = Response(event_stream(), content_type="text/event-stream")
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['X-Accel-Buffering'] = 'no'
    return response

@app.route("/")
def home():
    return "<h1>Arpan Flask App</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000,threaded=True)