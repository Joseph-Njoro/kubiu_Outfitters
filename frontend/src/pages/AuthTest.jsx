// src/pages/AuthTest.jsx

import React, { useEffect, useState } from 'react';
import authService from '../services/authService';

const AuthTest = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProtectedData = async () => {
      try {
        // Await the headers to ensure async operations are handled
        const headers = await authService.getAuthHeaders();

        const response = await fetch('http://localhost:8000/api/api/protected/', {
          headers: {
            ...headers,
            'Content-Type': 'application/json' // Ensure correct content type
          },
        });

        if (response.ok) {
          const result = await response.json();
          setData(result);
        } else {
          const errorData = await response.json();
          setError(errorData.detail || 'Failed to fetch protected data');
        }
      } catch (err) {
        setError('An error occurred');
        console.error(err);
      }
    };

    fetchProtectedData();
  }, []);

  return (
    <div>
      <h2>Auth Test</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
};

export default AuthTest;