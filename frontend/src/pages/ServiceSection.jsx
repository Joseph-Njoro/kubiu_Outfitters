// src/pages/ServiceSection.jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const ServiceSection = () => {
  const [services, setServices] = useState([]);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await fetch('/api/api/services/');
        if (!response.ok) {
          throw new Error('Failed to fetch services');
        }
        const data = await response.json();
        console.log('Fetched services:', data); // Log the fetched data for debugging
        setServices(data);
      } catch (error) {
        console.error('An error occurred while fetching services:', error);
      }
    };

    fetchServices();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Our Services</h2>
      <div className="row">
        {services.length > 0 ? (
          services.map(service => (
            <div className="col-md-4 mb-4" key={service.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{service.title}</h5>
                  <p className="card-text">{service.description}</p>
                  <p className="card-text"><strong>Price:</strong> ${service.price ? service.price.toFixed(2) : 'N/A'}</p>
                  {/* Add any additional service details or features here */}
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No services available at the moment.</p>
        )}
      </div>
    </div>
  );
};

export default ServiceSection;