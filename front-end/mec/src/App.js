import React from "react";
import { Routes, Route } from "react-router-dom"
import logo from './logo.svg';
import Test from './test.js';
import Main from './main.js';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/dev" element={<Test />} />
      </Routes>
    </div>
  );
}

export default App;
