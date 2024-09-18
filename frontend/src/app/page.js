
"use client"

import { useState, useEffect, useCallback } from 'react';

export default function Home() {


  
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);




  const connectToSSE = useCallback(() => {
    const eventSource = new EventSource('http://127.0.0.1:5000/stream');

    eventSource.onopen = () => {
      console.log('Connected to server');
      setIsLoading(false);
      setError(null);
    };

    eventSource.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      console.log('New data received:', newData);
      setData(newData);
    };

    eventSource.onerror = (error) => {
      console.error('EventSource failed:', error);
      setError('Connection to server lost. Attempting to reconnect...');
      setIsLoading(true);
      eventSource.close();
      setTimeout(connectToSSE, 5000); // Try to reconnect after 5 seconds
    };

    return eventSource;
  }, []);




  useEffect(() => {
    const eventSource = connectToSSE();

    return () => {
      eventSource.close();
    };
  }, [connectToSSE]);








  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Real-time Data from Flask Backend:</h1>
      {isLoading && <p className="text-gray-500">Connecting to server...</p>}
      {error && <p className="text-red-500">{error}</p>}
      <ul className="space-y-2">
        {data.map((item) => (
          <li key={item.id} className="bg-gray-100 p-2 rounded">
            <span className="font-semibold">{item.keyword}</span>
            <p className="text-sm text-gray-600">{item.title}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}