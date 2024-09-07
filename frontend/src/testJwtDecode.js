import jwtDecode from 'jwt-decode'; // Default import

// Sample token (replace with a real JWT token for actual testing)
const sampleToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NjMzODY1LCJpYXQiOjE3MjU2MzM1NjUsImp0aSI6IjQyM2JlZDg3OGFhNTQ0OTNiMTFlMjlhNzg4ZThmZTFkIiwidXNlcl9pZCI6MX0.fz2tRe2n1KHu0rmQeQ-Nf1mAJJySUXkTMWzuhi9N0ak';

try {
  const decoded = jwtDecode(sampleToken);
  console.log('Decoded JWT:', decoded);
} catch (error) {
  console.error('Error decoding JWT:', error);
}