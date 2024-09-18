import sqlite3
import schedule
import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
# Define your function to fetch responses from the database
def fetch_all_responses():
    conn = sqlite3.connect(r'C:\Users\p\Documents\estudios\01\projects\react_cron_jobs_backend\articles_kw_data.db')
    cursor = conn.execute('SELECT id, title, creation_date, keyword FROM articles_kw_data')
    responses = []
    for row in cursor:
        response = {
            "id": row[0],
            "title": row[1],
            "creation_date": row[2],
            "keyword": row[3]
        }
        responses.append(response)
        #print(f"ID: {row[0]}, Title: {row[1]}, Date: {row[2]}, Keyword: {row[3]}")
    conn.close()
    return responses




# Cron job to fetch and print responses from the database every 10 seconds
def cron_task():
    print("Cron job running: Fetching all responses from the database...")
    global a, b  

    print("a b ", a, b)

    a, b = 12, 16
    print("a b ", a, b)





# Set up a cron job to run every 10 seconds
schedule.every(10).seconds.do(cron_task)




a, b = 2, 6
# Flask route to allow React frontend to fetch responses from the database
@app.route("/api/data", methods=['GET'])
def get_responses1():
    print("pre REsssssssssssss")
    global a, b
    responses = fetch_all_responses()  # Reuse the same function to fetch responses for the API
    #print(responses,"REsssssssssssss")
    responses = responses[a:b]
    print("responses", responses, a, b)

    a, b = 2, 6

    return jsonify(responses)


@app.route("/")
def get_responses():
    print("pre REsssssssssssss")

    #responses = fetch_all_responses()  # Reuse the same function to fetch responses for the API
    #print(responses,"REsssssssssssss")

    return "<h1>Arpan  Flask App</h1>"
# Function to run the scheduler in a separate thread


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the Flask app and the scheduler
if __name__ == "__main__":
    from threading import Thread
    t = Thread(target=run_scheduler)
    t.start()
    app.run(debug=True)
