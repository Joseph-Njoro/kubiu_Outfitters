// src/pages/Contact.jsx
import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Contact.css';
import contactService from '../services/contactService';

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        subject: '',
        message: ''
    });

    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [errors, setErrors] = useState({});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const validateForm = () => {
        const newErrors = {};
        if (!formData.name) newErrors.name = 'Name is required';
        if (!formData.email) newErrors.email = 'Email is required';
        else if (!/\S+@\S+\.\S+/.test(formData.email)) newErrors.email = 'Email is invalid';
        if (!formData.phone) newErrors.phone = 'Phone number is required';
        if (!formData.subject) newErrors.subject = 'Subject is required';
        if (formData.message.length < 10) newErrors.message = 'Message must be at least 10 characters long';

        return newErrors;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const validationErrors = validateForm();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }

        try {
            await contactService.submitContactForm(formData);
            setSuccessMessage('Your message has been sent!');
            setErrorMessage('');
            setFormData({
                name: '',
                email: '',
                phone: '',
                subject: '',
                message: ''
            });
        } catch (error) {
            setErrorMessage('There was an error sending your message.');
            setSuccessMessage('');
        }
    };

    return (
        <div className="container mt-5">
            <h2>Contact Us</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="name">Name</label>
                    <input
                        type="text"
                        className={`form-control ${errors.name ? 'is-invalid' : ''}`}
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />
                    {errors.name && <div className="invalid-feedback">{errors.name}</div>}
                </div>

                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        className={`form-control ${errors.email ? 'is-invalid' : ''}`}
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                    {errors.email && <div className="invalid-feedback">{errors.email}</div>}
                </div>

                <div className="form-group">
                    <label htmlFor="phone">Phone</label>
                    <input
                        type="tel"
                        className={`form-control ${errors.phone ? 'is-invalid' : ''}`}
                        id="phone"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                    />
                    {errors.phone && <div className="invalid-feedback">{errors.phone}</div>}
                </div>

                <div className="form-group">
                    <label htmlFor="subject">Subject</label>
                    <input
                        type="text"
                        className={`form-control ${errors.subject ? 'is-invalid' : ''}`}
                        id="subject"
                        name="subject"
                        value={formData.subject}
                        onChange={handleChange}
                    />
                    {errors.subject && <div className="invalid-feedback">{errors.subject}</div>}
                </div>

                <div className="form-group">
                    <label htmlFor="message">Message</label>
                    <textarea
                        className={`form-control ${errors.message ? 'is-invalid' : ''}`}
                        id="message"
                        name="message"
                        rows="5"
                        value={formData.message}
                        onChange={handleChange}
                    ></textarea>
                    {errors.message && <div className="invalid-feedback">{errors.message}</div>}
                </div>

                <button type="submit" className="btn btn-primary mt-3">Submit</button>
            </form>

            {successMessage && <div className="alert alert-success mt-3">{successMessage}</div>}
            {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
        </div>
    );
};

export default Contact;