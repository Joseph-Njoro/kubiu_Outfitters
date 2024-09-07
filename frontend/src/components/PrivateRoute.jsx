// src/components/PrivateRoute.jsx
import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import authService from '../services/authService';

const PrivateRoute = ({ children }) => {
  const location = useLocation(); // Get the current location

  // Check if the user is authenticated
  if (authService.isAuthenticated()) {
    return children; // Render children if authenticated
  }

  // Redirect to the login page with the current location
  return <Navigate to="/login" state={{ from: location }} />;
};

export default PrivateRoute;