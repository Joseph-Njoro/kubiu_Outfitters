// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavbarComponent from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Contact from './pages/Contact';
import ExampleComponent from './pages/ExampleComponent';
import GalleryCarousel from './components/GalleryCarousel';
import './App.css';

const App = () => {
  return (
    <Router>
      <NavbarComponent />
      <div>
        {/* Add your gallery carousel here */}
        <GalleryCarousel />
      </div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/example" element={<ExampleComponent />} />
        {/* Define additional routes if needed */}
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;