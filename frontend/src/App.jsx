import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavbarComponent from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Contact from './pages/Contact';
import ExampleComponent from './pages/ExampleComponent';
import BlogPosts from './pages/BlogPosts';
import BlogPostDetail from './pages/BlogPostDetail';
import ServiceSection from './pages/ServiceSection';
import LoginPage from './pages/LoginPage';
import AuthTest from './pages/AuthTest'; // Import AuthTest component
import PrivateRoute from './components/PrivateRoute';
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
          <Route path="/login" element={<LoginPage />} />
          <Route path="/auth-test" element={<AuthTest />} />
          <Route 
            path="/services" 
            element={
              <PrivateRoute>
                <ServiceSection />
              </PrivateRoute>
            } 
          />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
};

export default App;