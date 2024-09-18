

"use client"


import { useState, useEffect } from 'react';

export default function Home() {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await fetch("http://127.0.0.1:5000/api/data");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const newData = await response.json();
      console.log(newData, "New data fetched:");
      setData(newData);
      setError(null);
    } catch (error) {
      console.error("Error fetching data:", error);
      setError("Failed to fetch data. Please try again later.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const intervalId = setInterval(fetchData, 10000); // Fetch every 10 seconds

    return () => clearInterval(intervalId); // Cleanup on unmount
  }, []);

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Data from Flask Backend:</h1>
      {isLoading && <p className="text-gray-500">Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      {!isLoading && !error && (
        <>
          <ul className="space-y-2">
            {data.map((item) => (
              <li key={item.id} className="bg-gray-100 p-2 rounded">
                <span className="font-semibold">{item.keyword}</span>
                <p className="text-sm text-gray-600">{item.title}</p>
              </li>
            ))}
          </ul>
          <button 
            onClick={fetchData} 
            className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Refresh Data
          </button>
        </>
      )}
    </div>
  );
}