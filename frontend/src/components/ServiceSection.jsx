// src/components/ServiceSection.jsx
import React, { useState, useEffect } from 'react';
import { Card, Col, Row } from 'react-bootstrap';
import authService from '../services/authService'; // Import your auth service

const ServiceSection = () => {
    const [services, setServices] = useState([]);

    // Fetch services from backend
    const fetchServices = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/api/services/', {
                headers: authService.getAuthHeaders(), // Use authService to get headers
            });

            if (!response.ok) {
                if (response.status === 401) {
                    // Handle token refresh logic here
                    await authService.refreshToken();
                    // Retry the request after refreshing the token
                    return fetchServices();
                }
                throw new Error('Failed to fetch services');
            }

            const contentType = response.headers.get('Content-Type');
            if (!contentType || !contentType.includes('application/json')) {
                throw new Error('Expected JSON response');
            }

            const data = await response.json();
            setServices(data);
        } catch (error) {
            console.error('An error occurred while fetching services:', error);
        }
    };

    // Fetch services on component mount
    useEffect(() => {
        fetchServices();
    }, []);

    return (
        <div className="container mt-4">
            <h2 className="mb-4">Our Services</h2>
            <Row>
                {services.map(service => (
                    <Col md={4} key={service.id} className="mb-4">
                        <Card>
                            <Card.Body>
                                <Card.Title>{service.name}</Card.Title>
                                <Card.Text>{service.description}</Card.Text>
                                <Card.Text><strong>Price:</strong> ${service.pricing}</Card.Text>
                                <div className="d-flex">
                                    {service.features.map((feature, index) => (
                                        <div key={index} className="me-2">
                                            <i className="bi bi-check-circle"></i> {feature}
                                        </div>
                                    ))}
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </div>
    );
};

export default ServiceSection;