// src/store/rootReducer.js
import { combineReducers } from 'redux';
import exampleReducer from './exampleReducer'; // Import the example reducer

// Combine reducers into a root reducer
const rootReducer = combineReducers({
  example: exampleReducer, // Add your reducers here
});

export default rootReducer;