import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  return (
    <div className="flex justify-center items-center h-screen">
      <Evaluator />
    </div>
  );
}

function Evaluator() {
  const [prefixInput, setPrefixInput] = useState("");
  const [postfixInput, setPostfixInput] = useState("");
  const [prefixOutput, setPrefixOutput] = useState("");
  const [postfixOutput, setPostfixOutput] = useState("");
  const [prefixSteps, setPrefixSteps] = useState([]);
  const [postfixSteps, setPostfixSteps] = useState([]);

  const evaluateExpression = async (expression, notation) => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/evaluate", { expression, notation }, { headers: { "Content-Type": "application/json" } });
      return { result: response.data.result, steps: response.data.steps };
    } catch (error) {
      return { result: "Error occurred", steps: [] };
    }
  };

  const handlePrefixSubmit = async () => {
    const { result, steps } = await evaluateExpression(prefixInput, "prefix");
    setPrefixOutput(result);
    setPrefixSteps(steps);
  };

  const handlePostfixSubmit = async () => {
    const { result, steps } = await evaluateExpression(postfixInput, "postfix");
    setPostfixOutput(result);
    setPostfixSteps(steps);
  };

  return (
    <div className="flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-10">Prefix and Postfix Evaluator</h1>
      <div className="flex flex-row justify-center p-4 gap-5 bg-white shadow-lg rounded-lg">
        <ExpressionEvaluator
          title="Prefix"
          inputValue={prefixInput}
          setInputValue={setPrefixInput}
          handleSubmit={handlePrefixSubmit}
          outputValue={prefixOutput}
          steps={prefixSteps}
        />
        <ExpressionEvaluator
          title="Postfix"
          inputValue={postfixInput}
          setInputValue={setPostfixInput}
          handleSubmit={handlePostfixSubmit}
          outputValue={postfixOutput}
          steps={postfixSteps}
        />
      </div>
    </div>
  );
}

function ExpressionEvaluator({ title, inputValue, setInputValue, handleSubmit, outputValue, steps }) {
  return (
    <div className="flex flex-col items-center p-4 border rounded-md shadow-lg">
      <h2 className="text-xl font-semibold mb-4">{title}</h2>
      <input
        type="text"
        placeholder={`Enter ${title.toLowerCase()} expression`}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        className="border p-2 rounded w-full mb-4"
      />
      <button
        onClick={handleSubmit}
        className={`bg-${title === "Prefix" ? "blue" : "green"}-500 text-white px-4 py-2 rounded mb-4 hover:bg-${title === "Prefix" ? "blue" : "green"}-600`}
      >
        Evaluate
      </button>
      <input
        type="text"
        value={outputValue}
        readOnly
        className="border p-2 rounded w-full bg-black text-white"
      />
      <StackVisualization steps={steps} />
    </div>
  );
}

function StackVisualization({ steps }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    steps.forEach((step, index) => {
      setTimeout(() => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "black";
        ctx.font = "16px Arial";
        ctx.fillText(`Step ${index + 1}:`, 10, 20);
        
        const stackValues = step.match(/-?\d+/g) || [];
        stackValues.reverse();
        stackValues.forEach((value, i) => {
          ctx.fillStyle = "#4CAF50";
          ctx.fillRect(50, 50 + i * 30, 50, 25);
          ctx.fillStyle = "white";
          ctx.fillText(value, 70, 68 + i * 30);
        });
      }, index * 1200);
    });
  }, [steps]);

  return <canvas ref={canvasRef} width={200} height={300} className="border mt-4" />;
}

export default App;
