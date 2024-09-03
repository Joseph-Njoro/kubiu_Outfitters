// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavbarComponent from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Contact from './pages/Contact';
import ExampleComponent from './pages/ExampleComponent';
import BlogPosts from './pages/BlogPosts'; // Import BlogPosts component
import BlogPostDetail from './pages/BlogPostDetail'; // Import BlogPostDetail component
import './App.css';

const App = () => {
  return (
    <Router>
      <NavbarComponent />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/example" element={<ExampleComponent />} />
        <Route path="/blog" element={<BlogPosts />} />
        <Route path="/blog/:id" element={<BlogPostDetail />} />
        {/* Define additional routes if needed */}
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;