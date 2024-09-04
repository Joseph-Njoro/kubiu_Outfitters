// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavbarComponent from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Contact from './pages/Contact';
import ExampleComponent from './pages/ExampleComponent';
import LogoutButton from './components/LogoutButton'; // Include logout button
import BlogPosts from './pages/BlogPosts'; // Import BlogPosts component
import BlogPostDetail from './pages/BlogPostDetail'; // Import BlogPostDetail component
import ServiceSection from './pages/ServiceSection'; // Import ServiceSection component
import LoginPage from './pages/LoginPage'; // Import LoginPage component
import './App.css';

const App = () => {
  return (
    <Router>
      <NavbarComponent />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/example" element={<ExampleComponent />} />
          <Route path="/blog" element={<BlogPosts />} />
          <Route path="/blog/:id" element={<BlogPostDetail />} />
          <Route path="/services" element={<ServiceSection />} />
          <Route path="/login" element={<LoginPage />} /> {/* Add the new route for login */}
          {/* Define additional routes if needed */}
        </Routes>
      </div>
      <Footer />
      <LogoutButton /> {/* Add LogoutButton component */}
    </Router>
  );
};

export default App;
