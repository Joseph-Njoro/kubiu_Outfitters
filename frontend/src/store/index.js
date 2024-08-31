// src/store/index.js
import { createStore } from 'redux';
import rootReducer from './rootReducer';

// Create the Redux store
const store = createStore(rootReducer);

export default store;