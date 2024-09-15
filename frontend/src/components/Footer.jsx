// src/components/Footer.jsx
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Footer.css';
const Footer = () => {
  return (
    <footer className="bg-light text-center text-lg-start">
      <div className="container p-4">
        <div className="row">
          <div className="col-lg-6 col-md-12 mb-4 mb-md-0">
            <h5 className="text-uppercase">Kubiu Outfitters</h5>
            <p>
              © 2024 Kubiu Outfitters. All rights reserved.
            </p>
          </div>
          <div className="col-lg-6 col-md-12 mb-4 mb-md-0">
            <ul className="list-unstyled mb-0">
              <li>
                <a href="/" className="text-dark">Home</a>
              </li>
              <li>
                <a href="/services" className="text-dark">Services</a>
              </li>
              <li>
                <a href="/portfolio" className="text-dark">Portfolio</a>
              </li>
              <li>
                <a href="/contact" className="text-dark">Contact</a>
              </li>
              <li>
                <a href="/example" className="text-dark">Example</a>
              </li>
              <li>
                <a href="/blog" className="text-dark">Blog Posts</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;