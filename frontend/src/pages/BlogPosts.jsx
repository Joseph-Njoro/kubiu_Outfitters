import React, { useState, useEffect, useCallback } from 'react';
import BlogPostCard from '../components/BlogPostCard';

const BlogPosts = () => {
    const [posts, setPosts] = useState([]);
    const [page, setPage] = useState(1);
    const [hasMore, setHasMore] = useState(true);

    const fetchBlogPosts = useCallback(async (pageNumber) => {
        try {
            const response = await fetch(`/api/api/blogposts/?page=${pageNumber}`);
            if (!response.ok) {
                throw new Error('Failed to fetch blog posts');
            }
            const data = await response.json();
            setPosts(prevPosts => [...prevPosts, ...data.results]);
            setHasMore(data.results.length > 0);
        } catch (error) {
            console.error('An error occurred while fetching blog posts:', error);
        }
    }, []);

    useEffect(() => {
        fetchBlogPosts(page);
    }, [page, fetchBlogPosts]);

    const handleScroll = () => {
        if (window.innerHeight + document.documentElement.scrollTop !== document.documentElement.offsetHeight || !hasMore) return;
        setPage(prevPage => prevPage + 1);
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, [handleScroll]);

    return (
        <div className="container mt-4">
            <div className="row">
                {posts.map(post => (
                    <BlogPostCard key={post.id} post={post} />
                ))}
            </div>
            {!hasMore && <p>No more posts to load.</p>}
        </div>
    );
};

export default BlogPosts;
