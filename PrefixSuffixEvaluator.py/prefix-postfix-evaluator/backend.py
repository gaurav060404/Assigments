from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

def evaluate_prefix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    tokens = expression.split()
    reversed_list = reversed(tokens)
    steps = []
    for token in reversed_list:
        if token not in operators:
            stack.append(int(token))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = eval(f"{op1} {token} {op2}")
            stack.append(result)
        steps.append(f"Stack: {stack}")
    return stack.pop(), steps

def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    steps = []
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = eval(f"{op1} {token} {op2}")
            stack.append(result)
        steps.append(f"Stack: {stack}")
    return stack.pop(), steps

@app.route('/evaluate', methods=['POST'])
def evaluate_expression():
    data = request.get_json()
    expression = data.get("expression")
    notation = data.get("notation")  

    if not expression or notation not in ["prefix", "postfix"]:
        return jsonify({"error": "Invalid input"}), 400

    try:
        result, steps = evaluate_prefix(expression) if notation == "prefix" else evaluate_postfix(expression)
        return jsonify({"result": result, "steps": steps})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
