# Real-time Data Stream Application

 real-time data streaming between a Python Flask backend and a React frontend.

## Project Structure

- **Backend**: Python (Flask)
- **Frontend**: React (Next.js)



## KEY CONFIGURATIION:

  "proxy" : "http://localhost:5000",

## Features

### Backend (Flask)
- Connects to an SQLite database (`articles_kw_data.db`), fetching article data (ID, title, creation date, and keyword).
- Provides two routes:
  1. `/api/data`: Returns a random slice of 5 article entries in JSON format.
  2. `/stream`: Streams real-time updates of the article data every 10 seconds using **Server-Sent Events (SSE)**.
- CORS enabled to allow connections from `localhost:3000` (React frontend).

### Frontend (React)
- Connects to the Flask backend using **SSE** for real-time updates.
- Displays the article data with titles and keywords in a responsive UI.
- Automatically reconnects to the backend in case of connection loss.

## Setup

### Backend (Flask)

1. Install dependencies:
   ```bash
   pip install flask flask-cors
