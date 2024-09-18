Real-time Data Stream Application
This project demonstrates a full-stack application that provides real-time data streaming between a Python Flask backend and a React frontend.

Project Structure
Backend: Python (Flask)
Frontend: React (Next.js)
Features
Backend (Flask)
Connects to an SQLite database (articles_kw_data.db), fetching article data (ID, title, creation date, and keyword).
Provides two routes:
/api/data: Returns a random slice of 5 article entries in JSON format.
/stream: Streams real-time updates of the article data every 10 seconds using Server-Sent Events (SSE).
CORS enabled to allow connections from localhost:3000 (React frontend).
Frontend (React)
Connects to the Flask backend using SSE for real-time updates.
Displays the article data with titles and keywords in a responsive UI.
Automatically reconnects to the backend in case of connection loss.
Setup
Backend (Flask)
Install dependencies:
bash
Copy code
pip install flask flask-cors
Run the Flask server:
bash
Copy code
python app.py
Ensure SQLite database articles_kw_data.db is present at the specified path.
Frontend (React)
Install dependencies:
bash
Copy code
npm install
Start the React development server:
bash
Copy code
npm run dev
The frontend will attempt to connect to the backend at http://127.0.0.1:5000/stream.
