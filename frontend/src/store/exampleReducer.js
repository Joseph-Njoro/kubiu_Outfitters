// src/store/exampleReducer.js
import { SET_EXAMPLE_DATA } from './actions';

// Example reducer to handle actions
const exampleReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_EXAMPLE_DATA:
      return { ...state, data: action.payload };
    default:
      return state;
  }
};

export default exampleReducer;