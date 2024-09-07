// src/pages/ServiceSection.jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

// Sample data for sorting options
const SORT_OPTIONS = [
  { value: 'date_desc', label: 'Date: Newest to Oldest' },
  { value: 'date_asc', label: 'Date: Oldest to Newest' },
  { value: 'rating_desc', label: 'Rating: Highest to Lowest' },
  { value: 'rating_asc', label: 'Rating: Lowest to Highest' }
];

const ServiceSection = () => {
  const [testimonials, setTestimonials] = useState([]);
  const [sortOption, setSortOption] = useState('date_desc');
  
  useEffect(() => {
    const fetchTestimonials = async () => {
      try {
        const response = await fetch(`/api/api/testimonials/?sort=${sortOption}`);
        if (!response.ok) {
          throw new Error('Failed to fetch testimonials');
        }
        const data = await response.json();
        console.log('Fetched testimonials:', data); // Log the fetched data for debugging
        setTestimonials(data);
      } catch (error) {
        console.error('An error occurred while fetching testimonials:', error);
      }
    };

    fetchTestimonials();
  }, [sortOption]); // Fetch testimonials whenever sortOption changes

  const handleSortChange = (event) => {
    setSortOption(event.target.value);
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Customer Testimonials</h2>
      
      {/* Sorting Options */}
      <div className="mb-4">
        <label htmlFor="sort" className="form-label">Sort By:</label>
        <select id="sort" className="form-select" value={sortOption} onChange={handleSortChange}>
          {SORT_OPTIONS.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </div>
      
      <div className="row">
        {testimonials.length > 0 ? (
          testimonials.map(testimonial => (
            <div className="col-md-4 mb-4" key={testimonial.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{testimonial.clientName}</h5>
                  <p className="card-text">
                    <strong>Rating:</strong> {testimonial.rating}
                  </p>
                  <p className="card-text">{testimonial.feedback}</p>
                  <p className="card-text"><strong>Date:</strong> {new Date(testimonial.date).toLocaleDateString()}</p>
                  {/* Add any additional testimonial details or features here */}
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No testimonials available at the moment.</p>
        )}
      </div>
    </div>
  );
};

export default ServiceSection;