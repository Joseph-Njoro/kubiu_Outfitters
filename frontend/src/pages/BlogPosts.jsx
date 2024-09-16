import React, { useState, useEffect, useCallback } from 'react';
import BlogPostCard from '../components/BlogPostCard';
import '../styles/BlogPosts.css';

const BlogPosts = () => {
    const [posts, setPosts] = useState([]);
    const [page, setPage] = useState(1);
    const [hasMore, setHasMore] = useState(true);
    const [loading, setLoading] = useState(false); // Track loading state
    const [error, setError] = useState(null); // Track error state

    // Fetch blog posts with pagination
    const fetchBlogPosts = useCallback(async (pageNumber) => {
        setLoading(true); // Start loading
        setError(null); // Reset error state
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/api/blogposts/?page=${pageNumber}`);
            if (!response.ok) {
                throw new Error('Failed to fetch blog posts');
            }
            const data = await response.json();
            
            // Deduplicate posts
            setPosts(prevPosts => {
                const existingPostIds = new Set(prevPosts.map(post => post.id));
                const newPosts = data.results.filter(post => !existingPostIds.has(post.id));
                return [...prevPosts, ...newPosts];
            });

            setHasMore(data.next !== null); // Set hasMore based on 'next' link
        } catch (error) {
            setError(error.message); // Set error message
            console.error('An error occurred while fetching blog posts:', error);
        } finally {
            setLoading(false); // End loading
        }
    }, []);

    // Fetch blog posts on page change
    useEffect(() => {
        fetchBlogPosts(page);
    }, [page, fetchBlogPosts]);

    // Handle infinite scrolling
    const handleScroll = () => {
        if (window.innerHeight + document.documentElement.scrollTop !== document.documentElement.offsetHeight || !hasMore || loading) return;
        setPage(prevPage => prevPage + 1);
    };

    // Attach scroll event listener
    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, [handleScroll, hasMore, loading]);

    return (
        <div className="container mt-4">
            <div className="row">
                {posts.map(post => (
                    <BlogPostCard key={post.id} post={post} />
                ))}
            </div>
            {loading && <p>Loading more posts...</p>} {/* Loading message */}
            {error && <p className="error-message">{error}</p>} {/* Error message */}
            {!hasMore && !loading && <p>No more posts to load.</p>}
        </div>
    );
};

export default BlogPosts;