// jwtDecode.js

/**
 * Decodes a JWT token and returns the payload.
 * @param {string} token - The JWT token to decode.
 * @returns {object} - The decoded payload.
 */
export function jwtDecode(token) {
  if (!token) {
    throw new Error('No token provided');
  }

  // Split the token into its parts
  const parts = token.split('.');

  if (parts.length !== 3) {
    throw new Error('JWT does not have 3 parts');
  }

  // Decode the payload (second part) from base64url
  const payload = parts[1];
  const decodedPayload = atob(payload.replace(/-/g, '+').replace(/_/g, '/'));

  try {
    return JSON.parse(decodedPayload);
  } catch (e) {
    throw new Error('Failed to parse JWT payload');
  }
}
