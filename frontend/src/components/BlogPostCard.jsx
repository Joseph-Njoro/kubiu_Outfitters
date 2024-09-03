// src/components/BlogPostCard.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const BlogPostCard = ({ post }) => {
    return (
        <div className="col-md-4 mb-4">
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title">{post.title}</h5>
                    <h6 className="card-subtitle mb-2 text-muted">{post.author} - {new Date(post.published_at).toLocaleDateString()}</h6>
                    <p className="card-text">{post.summary}</p>
                    <Link to={`/blog/${post.id}`} className="btn btn-primary">Read More</Link>
                </div>
            </div>
        </div>
    );
};

export default BlogPostCard;