import React, { useState, useEffect } from 'react';

const GalleryCarousel = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        const fetchGalleryImages = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/api/portfolios/');
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
                        <img
                            src={image.image}
                            className="d-block w-100"
                            alt={image.description}
                            style={{
                                objectFit: 'contain', // Maintain aspect ratio
                                width: '100%', // Make the width 100% of the container
                                maxHeight: '780px', // Specify the maximum height
                                height: 'auto' // Allow height to auto adjust
                            }}
                        />
                        <div
                            className="carousel-caption d-none d-md-block"
                            style={{
                                background: 'rgba(0, 0, 0, 0.5)', // Semi-transparent background
                                padding: '10px',
                                borderRadius: '5px',
                                bottom: '20px',
                                left: '0',
                                right: '0',
                                textAlign: 'center'
                            }}
                        >
                            <h5 style={{ color: '#fff', fontSize: '1.5rem' }}>{image.title}</h5>
                            <p style={{ color: '#fff', fontSize: '1rem' }}>{image.description}</p>
                            {image.tags && image.tags.length > 0 && (
                                <div style={{ marginTop: '10px' }}>
                                    {image.tags.map((tag, tagIndex) => (
                                        <span
                                            key={tagIndex}
                                            style={{
                                                backgroundColor: '#007bff',
                                                color: '#fff',
                                                padding: '5px 10px',
                                                borderRadius: '5px',
                                                marginRight: '5px',
                                                fontSize: '0.9rem'
                                            }}
                                        >
                                            {tag}
                                        </span>
                                    ))}
                                </div>
                            )}
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