import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const BlogPostDetail = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [error, setError] = useState(null); // Added error state

  useEffect(() => {
    const fetchPostDetail = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/api/blogposts/${id}/`); // Ensure URL is correct
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setPost(data);
      } catch (error) {
        setError('An error occurred while fetching the blog post.');
        console.error('An error occurred while fetching the blog post:', error);
      }
    };

    fetchPostDetail();
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!post) return <p>Loading...</p>;

  return (
    <div className="container mt-4">
      <h1>{post.title}</h1>
      <p><strong>Author:</strong> {post.author}</p>
      <p><strong>Date:</strong> {new Date(post.published_at).toLocaleDateString()}</p> {/* Changed date field */}
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </div>
  );
};

export default BlogPostDetail;