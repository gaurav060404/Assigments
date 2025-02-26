from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

def evaluate_prefix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    reversed_expression = reversed(expression)
    reversed_list = reversed_expression.split()
    for token in reversed_list:
        if token not in operators:
            stack.append(int(token))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = eval(f"{op1} {token} {op2}")
            stack.append(result)
    return stack.pop()

def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = eval(f"{op1} {token} {op2}")
            stack.append(result)
    return stack.pop()

@app.route('/evaluate', methods=['POST'])
def evaluate_expression():
    data = request.get_json()
    expression = data.get("expression")
    notation = data.get("notation")  

    if not expression or notation not in ["prefix", "postfix"]:
        return jsonify({"error": "Invalid input"}), 400

    try:
        result = evaluate_prefix(expression) if notation == "prefix" else evaluate_postfix(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
