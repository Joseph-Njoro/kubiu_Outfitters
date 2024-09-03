// src/pages/Home.jsx
import React from 'react';
import GalleryCarousel from '../components/GalleryCarousel';

const Home = () => {
  return (
    <div>
      <GalleryCarousel /> {/* Only include here */}
      <h1>Home Page</h1>
      {/* Add other home page content here */}
    </div>
  );
};

export default Home;