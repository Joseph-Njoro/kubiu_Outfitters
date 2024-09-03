import React, { useState, useEffect } from 'react';

const GalleryCarousel = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        const fetchGalleryImages = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/api/portfolios/');  // Full URL with the base URL included
                if (!response.ok) {
                    throw new Error('Failed to fetch images');
                }
                const data = await response.json();
                setImages(data.results);
            } catch (error) {
                console.error('An error occurred while fetching gallery images:', error);
            }
        };

        fetchGalleryImages();
    }, []);

    return (
        <div id="galleryCarousel" className="carousel slide" data-bs-ride="carousel">
            <div className="carousel-inner">
                {images.map((image, index) => (
                    <div key={index} className={`carousel-item ${index === 0 ? 'active' : ''}`}>
                        <img src={image.image} className="d-block w-100" alt={image.description} />
                        <div className="carousel-caption d-none d-md-block">
                            <h5>{image.title}</h5>
                            <p>{image.description}</p>
                        </div>
                    </div>
                ))}
            </div>
            <button className="carousel-control-prev" type="button" data-bs-target="#galleryCarousel" data-bs-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Previous</span>
            </button>
            <button className="carousel-control-next" type="button" data-bs-target="#galleryCarousel" data-bs-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Next</span>
            </button>
        </div>
    );
};

export default GalleryCarousel;