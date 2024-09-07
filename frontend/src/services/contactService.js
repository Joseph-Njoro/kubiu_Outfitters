const API_URL = 'http://localhost:8000/api/api/contacts/'; // Make sure this URL is correct

const contactService = {
  submitContactForm: async (formData) => {
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Check if the response is not OK (status code not in 200–299 range)
      if (!response.ok) {
        // Attempt to parse JSON, but it may also be HTML (like a 404 error page)
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Failed to submit the contact form');
        } else {
          const errorText = await response.text();
          throw new Error('Unexpected response: ' + errorText);
        }
      }

      // If everything is OK, parse the response as JSON
      return await response.json();
    } catch (error) {
      // Catch and throw the error to be handled in the component
      console.error('Error in contactService:', error);
      throw error;
    }
  },
};

export default contactService;