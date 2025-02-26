import React from 'react';
import './App.css';
import { useState } from "react";

function App() {
  return (
    <div className="flex justify-center align-center">
      <Evaluator/>
    </div>
  );
}

function Evaluator() {
  const [prefixInput, setPrefixInput] = useState("");
  const [postfixInput, setPostfixInput] = useState("");
  const [prefixOutput, setPrefixOutput] = useState("");
  const [postfixOutput, setPostfixOutput] = useState("");

  const evaluateExpression = async (expression, notation) => {
    const response = await fetch("http://localhost:5000/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ expression, notation })
    });
    const data = await response.json();
    return data.result || data.error;
  };

  const handlePrefixSubmit = async () => {
    const result = await evaluateExpression(prefixInput, "prefix");
    setPrefixOutput(result);
  };

  const handlePostfixSubmit = async () => {
    const result = await evaluateExpression(postfixInput, "postfix");
    setPostfixOutput(result);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen p-2">
      <h1 className="text-2xl font-bold mb-6">Prefix And Suffix Evaluator</h1>
      <div className="grid grid-cols-2 gap-10 p-6 bg-white shadow-lg rounded-lg">
        
        <div className="flex flex-col items-center p-4 border rounded-md">
          <h2 className="text-xl font-semibold mb-4">Prefix</h2>
          <input 
            type="text" 
            placeholder="Enter prefix expression"
            value={prefixInput}
            onChange={(e) => setPrefixInput(e.target.value)}
            className="border p-2 rounded w-full mb-4"
          />
          <button 
            onClick={handlePrefixSubmit}
            className="bg-blue-500 text-white px-4 py-2 rounded mb-4 hover:bg-blue-600"
          >
            Evaluate
          </button>
          <input 
            type="text" 
            value={prefixOutput} 
            readOnly 
            className="border p-2 rounded w-full bg-gray-200"
          />
        </div>
        
        <div className="flex flex-col items-center p-4 border rounded-md">
          <h2 className="text-xl font-semibold mb-4">Postfix</h2>
          <input 
            type="text" 
            placeholder="Enter postfix expression"
            value={postfixInput}
            onChange={(e) => setPostfixInput(e.target.value)}
            className="border p-2 rounded w-full mb-4"
          />
          <button 
            onClick={handlePostfixSubmit}
            className="bg-green-500 text-white px-4 py-2 rounded mb-4 hover:bg-green-600"
          >
            Evaluate
          </button>
          <input 
            type="text" 
            value={postfixOutput} 
            readOnly 
            className="border p-2 rounded w-full bg-gray-200"
          />
        </div>
      </div>
    </div>
  );
}

export default App;
