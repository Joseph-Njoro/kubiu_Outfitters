// src/store/actions.js
export const SET_EXAMPLE_DATA = 'SET_EXAMPLE_DATA';

// Action creator for setting example data
export const setExampleData = (data) => ({
  type: SET_EXAMPLE_DATA,
  payload: data,
});