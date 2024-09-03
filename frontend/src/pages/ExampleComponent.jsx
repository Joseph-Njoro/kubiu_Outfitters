// src/components/ExampleComponent.jsx
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setExampleData } from '../store/actions';

const ExampleComponent = () => {
  // Access state from the Redux store
  const exampleData = useSelector((state) => state.example.data);
  const dispatch = useDispatch();

  // Dispatch an action to update the state
  const handleUpdateData = () => {
    dispatch(setExampleData('New Data'));
  };

  return (
    <div>
      <h1>Example Data: {exampleData}</h1>
      <button onClick={handleUpdateData}>Update Data</button>
    </div>
  );
};

export default ExampleComponent;