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
  const [testimonials, setTestimonials] = useState({ results: [] });
  const [services, setServices] = useState({ results: [] }); // New state for services
  const [sortOption, setSortOption] = useState('date_desc');

  // Fetch testimonials
  useEffect(() => {
    const fetchTestimonials = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        const response = await fetch(`http://localhost:8000/api/api/testimonials/?sort=${sortOption}`, {
          headers: {
            'Authorization': `Bearer ${accessToken}`
          }
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Failed to fetch testimonials: ${response.status} ${errorText}`);
        }

        const data = await response.json();
        setTestimonials(data); // Set testimonials data
      } catch (error) {
        console.error('An error occurred while fetching testimonials:', error);
      }
    };

    fetchTestimonials();
  }, [sortOption]);

  // Fetch services
  useEffect(() => {
    const fetchServices = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        const response = await fetch('http://localhost:8000/api/api/services/', {
          headers: {
            'Authorization': `Bearer ${accessToken}`
          }
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Failed to fetch services: ${response.status} ${errorText}`);
        }

        const data = await response.json();
        setServices(data); // Set services data
      } catch (error) {
        console.error('An error occurred while fetching services:', error);
      }
    };

    fetchServices();
  }, []); // Fetch services on component mount

  const handleSortChange = (event) => {
    setSortOption(event.target.value);
  };

  return (
    <div className="container mt-4">
      {/* Services Section */}
      <h2 className="mb-4">Our Services</h2>
      <div className="row">
        {services.results && services.results.length > 0 ? (
          services.results.map(service => (
            <div className="col-md-4 mb-4" key={service.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{service.title}</h5>
                  <p className="card-text">{service.description}</p>
                  <p className="card-text"><strong>Price:</strong> {service.price}</p>
                  <p className="card-text"><strong>Date:</strong> {new Date(service.created_at).toLocaleDateString()}</p>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No services available at the moment.</p>
        )}
      </div>

      {/* Sorting Options for Testimonials */}
      <h2 className="mt-5 mb-4">Customer Testimonials</h2>
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

      {/* Testimonials Section */}
      <div className="row">
        {testimonials.results && testimonials.results.length > 0 ? (
          testimonials.results.map(testimonial => (
            <div className="col-md-4 mb-4" key={testimonial.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{testimonial.clientName}</h5>
                  <p className="card-text"><strong>Rating:</strong> {testimonial.rating}</p>
                  <p className="card-text">{testimonial.content}</p>
                  <p className="card-text"><strong>Date:</strong> {new Date(testimonial.created_at).toLocaleDateString()}</p>
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