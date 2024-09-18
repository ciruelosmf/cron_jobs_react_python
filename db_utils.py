import sqlite3
import json
from datetime import datetime

 

#conn = sqlite3.connect('articles_kw_data.db')  # Make sure you're connecting to the correct database
#cursor = conn.execute("SELECT * from articles_kw_data")

#tables = cursor.fetchall()
#print("Tables in the database:", tables)

#conn.close()

def fetch_all_responses():
    conn = sqlite3.connect(r'C:\Users\p\Documents\estudios\01\projects\react_cron_jobs_backend\articles_kw_data.db')
    cursor = conn.execute('SELECT id, title, creation_date, keyword FROM articles_kw_data')
    for row in cursor:
        print(f"ID: {row[0]}, Title: {row[1]}, Date: {row[2]}, Keyword: {row[3]}")
    conn.close()
fetch_all_responses()


"""   




def create_table_if_not_exists(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS articles_kw_data
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     json_data TEXT,
                     keyword TEXT,
                     title TEXT,
                     url TEXT,
                     creation_date TEXT)''')
    conn.commit()

def insert_json_response(conn, json_data, title, keyword, url):
    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute('INSERT INTO articles_kw_data (json_data, title, creation_date, keyword, url) VALUES (?, ?, ?, ?, ?)', 
                 (json.dumps(json_data), title, creation_date, keyword, url))
    conn.commit()



def fetch_all_responses():
    conn = sqlite3.connect('api_responses.db')
    cursor = conn.execute('SELECT id, title, creation_date, keyword FROM api_responses')
    for row in cursor:
        print(f"ID: {row[0]}, Title: {row[1]}, Date: {row[2]}, Keyword: {row[3]}")
    conn.close()

# Example usage
json_string = '{"posts": [{"title": "{article-title}", "h2-1": "{article-h2-1}", "h2-1-content": "{article-h2-1-content}", "h2-2": "{article-h2-2}", "h2-2-content": "{article-h2-2-content}", "h2-3": "{article-h2-3}", "h2-3-content": "{article-h2-3-content}", "url": "https://www.aiimageandvideogenerators.xyz/blog/{article-title-formatted-like-this}"}]}'
keyword = "example_keyword"
 






"""