import React, { useEffect } from 'react';
import '../styles/Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import GalleryCarousel from '../components/GalleryCarousel'; // Import the GalleryCarousel component
import { Link, useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const sections = document.querySelectorAll('.fade');
    const handleScroll = () => {
      sections.forEach((section) => {
        const sectionTop = section.getBoundingClientRect().top;
        if (sectionTop < window.innerHeight - 100) {
          section.classList.add('visible');
        }
      });
    };

    handleScroll();
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLoadMore = () => {
    navigate('/blog/');
  };

  return (
    <div className="home-container">
      {/* Welcome Section */}
      <section className="welcome-section">
        <h1 className="welcome-title">Welcome to Kubiu Outfitters</h1>
        <p className="welcome-quote">"Tailoring elegance for every occasion."</p>
        <Link to="/services">
          <button className="cta-button">Explore Our Services</button>
        </Link>
      </section>

      {/* Creative Message Section */}
      <section className="creative-message-section fade">
        <div className="creative-message">
          <h2 className="section-title">Stitched to Perfection</h2>
          <p className="message-text">
            "At Kubiu Outfitters, we don’t just make clothes; we craft masterpieces that make you look so good, even your mirror will do a double take! Check out our latest creations where threads meet trends, and your wardrobe gets a glow-up."
          </p>
        </div>
      </section>

      {/* Carousel Section */}
      <section className="carousel-section fade">
        <GalleryCarousel />
      </section>

      {/* Services Section */}
      <section className="services-section fade">
        <h2 className="section-title">Our Services</h2>
        <div className="creative-message">
          <h3 className="creative-message-title">Tailoring with a Twist!</h3>
          <p className="creative-message-text">
            "Our services are like a good suit—custom-fit, sharp, and always making an impression. Whether you need a fresh look or just a nip and tuck, we’ve got you covered. Because every outfit deserves a second chance... or a third!"
          </p>
        </div>
        <div className="card-deck">
          <div className="card service-card">
            <div className="card-body">
              <h3 className="card-title">Custom Tailoring</h3>
              <p className="card-text">We create bespoke outfits tailored to your style and fit.</p>
              <Link to="/services">
                <button className="cta-button">Learn More</button>
              </Link>
            </div>
          </div>
          <div className="card service-card">
            <div className="card-body">
              <h3 className="card-title">Alterations</h3>
              <p className="card-text">Perfect fit, every time. We offer professional alteration services.</p>
              <Link to="/services">
                <button className="cta-button">Learn More</button>
              </Link>
            </div>
          </div>
          <div className="card service-card">
            <div className="card-body">
              <h3 className="card-title">Styling Consultation</h3>
              <p className="card-text">Need fashion advice? Our experts are here to help.</p>
              <Link to="/services">
                <button className="cta-button">Learn More</button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="testimonials-section fade">
        <h2 className="section-title">Client Testimonials</h2>
        <div className="creative-message">
          <h3 className="creative-message-title">Don’t Just Take Our Word For It!</h3>
          <p className="creative-message-text">
            "Our clients say it best—our tailoring is so good, it could convince your grandmother you’re not the black sheep of the family! Read what others have to say and get inspired to join the ranks of the fashionably elite."
          </p>
        </div>
        <div className="card-deck">
          <div className="card testimonial-card">
            <div className="card-body">
              <p className="card-text">"Excellent service and great attention to detail!"</p>
              <Link to="/services" className="read-more">Read More</Link>
            </div>
          </div>
          <div className="card testimonial-card">
            <div className="card-body">
              <p className="card-text">"The best tailoring experience I've ever had."</p>
              <Link to="/services" className="read-more">Read More</Link>
            </div>
          </div>
          <div className="card testimonial-card">
            <div className="card-body">
              <p className="card-text">"High-quality craftsmanship and outstanding service."</p>
              <Link to="/services" className="read-more">Read More</Link>
            </div>
          </div>
        </div>
      </section>

      {/* Blog Section */}
      <section className="blog-section fade">
        <h2 className="section-title">Latest Blog Posts</h2>
        <div className="creative-message">
          <h3 className="creative-message-title">Threads and Trends!</h3>
          <p className="creative-message-text">
            "Dive into our blog where fashion meets fabric and trends are stitched with a side of wit. From timeless style tips to the latest in tailoring, our posts are as captivating as our creations. Because who says fashion can’t be educational and entertaining?"
          </p>
        </div>
        <div className="card-deck">
          <div className="card blog-card">
            <div className="card-body">
              <h3 className="card-title">How to Choose the Perfect Suit</h3>
              <p className="card-text">Choosing a suit that fits perfectly and suits your style can be challenging. Read our tips!</p>
              <button className="cta-button" onClick={handleLoadMore}>Read More</button>
            </div>
          </div>
          <div className="card blog-card">
            <div className="card-body">
              <h3 className="card-title">The Evolution of Tailoring</h3>
              <p className="card-text">Explore the history and evolution of tailoring through the ages.</p>
              <button className="cta-button" onClick={handleLoadMore}>Read More</button>
            </div>
          </div>
          <div className="card blog-card">
            <div className="card-body">
              <h3 className="card-title">Fashion Trends for 2024</h3>
              <p className="card-text">Stay ahead of the curve with our roundup of the hottest fashion trends for 2024.</p>
              <button className="cta-button" onClick={handleLoadMore}>Read More</button>
            </div>
          </div>
        </div>
      </section>


      {/* Contact Section */}
      <section className="contact-section fade">
        <h2 className="section-title">Contact Us</h2>
        <div className="creative-message">
          <h3 className="creative-message-title">Get in Touch, Don’t Be Shy!</h3>
          <p className="creative-message-text">
            "Have a question, a compliment, or just want to share your love for our tailoring? Drop us a line! We promise, our response time is faster than a tailor's needle in action!"
          </p>
        </div>
        <p className="contact-info">Get in touch for more information or to book a consultation.</p>
        <Link to="/contact">
          <button className="cta-button">Contact Us</button>
        </Link>
      </section>
    </div>
  );
};

export default Home;