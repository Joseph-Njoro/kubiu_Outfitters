import axios from 'axios';
import { jwtDecode } from './jwtDecode';

// Base URL for the Django API
const API_URL = 'http://localhost:8000/api/api';

// Auth service object
const authService = {
  // Handles user login and token storage
  login: async (email, password) => {
    try {
      const response = await axios.post(`${API_URL}/token/`, { email, password });
      const { access, refresh } = response.data;

      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);

      const user = jwtDecode(access);
      localStorage.setItem('user', JSON.stringify(user));

      return user;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },

  // Handles user logout by clearing tokens and user info
  logout: () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user');
  },

  // Retrieves the currently authenticated user from localStorage
  getCurrentUser: () => {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  },

  // Checks if the user is authenticated based on the presence of an accessToken
  isAuthenticated: () => {
    return !!localStorage.getItem('accessToken');
  },

  // Returns authorization headers including the accessToken
  getAuthHeaders: async () => {
    let accessToken = localStorage.getItem('accessToken');
    if (accessToken && isTokenExpired(accessToken)) {
      try {
        accessToken = await authService.refreshToken();
      } catch (error) {
        console.error('Error refreshing token:', error);
      }
    }
    return accessToken ? { Authorization: `Bearer ${accessToken}` } : {};
  },

  // Refreshes the access token using the refresh token
  refreshToken: async () => {
    const refreshToken = localStorage.getItem('refreshToken');
    if (!refreshToken) throw new Error('No refresh token available');

    try {
      const response = await axios.post(`${API_URL}/token/refresh/`, { refresh: refreshToken });
      const { access } = response.data;

      localStorage.setItem('accessToken', access);

      const user = jwtDecode(access);
      localStorage.setItem('user', JSON.stringify(user));

      return access;
    } catch (error) {
      console.error('Refresh token error:', error);
      throw error;
    }
  },
};

// Helper function to check if the token is expired
const isTokenExpired = (token) => {
  const decoded = jwtDecode(token);
  return decoded.exp < Date.now() / 1000;
};

export default authService;