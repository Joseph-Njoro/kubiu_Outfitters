// pages/TestimonialSection.jsx

import React, { useState, useEffect } from 'react';

const TestimonialSection = () => {
  const [testimonials, setTestimonials] = useState([]);
  const [sortedTestimonials, setSortedTestimonials] = useState([]);
  const [sortOption, setSortOption] = useState('date-desc'); // Default sort

  useEffect(() => {
    const fetchTestimonials = async () => {
      const response = await fetch('/api/api/testimonials/');
      const data = await response.json();
      setTestimonials(data);
      setSortedTestimonials(data);
    };

    fetchTestimonials();
  }, []);

  const handleSortChange = (event) => {
    const sortOption = event.target.value;
    setSortOption(sortOption);
    sortTestimonials(sortOption);
  };

  const sortTestimonials = (option) => {
    let sortedData = [...testimonials];
    switch (option) {
      case 'date-asc':
        sortedData.sort((a, b) => new Date(a.date) - new Date(b.date));
        break;
      case 'date-desc':
        sortedData.sort((a, b) => new Date(b.date) - new Date(a.date));
        break;
      case 'rating-asc':
        sortedData.sort((a, b) => a.rating - b.rating);
        break;
      case 'rating-desc':
        sortedData.sort((a, b) => b.rating - a.rating);
        break;
      default:
        break;
    }
    setSortedTestimonials(sortedData);
  };

  return (
    <div>
      <select onChange={handleSortChange} value={sortOption}>
        <option value="date-asc">Date: Oldest to Newest</option>
        <option value="date-desc">Date: Newest to Oldest</option>
        <option value="rating-asc">Rating: Lowest to Highest</option>
        <option value="rating-desc">Rating: Highest to Lowest</option>
      </select>
      <div>
        {sortedTestimonials.map(testimonial => (
          <div key={testimonial.id} className="card">
            <h3>{testimonial.name}</h3>
            <p>{testimonial.feedback}</p>
            <p>Rating: {testimonial.rating}</p>
            <p>Date: {new Date(testimonial.date).toLocaleDateString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TestimonialSection;
