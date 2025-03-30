from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print String Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print to console
    return text  # Display in browser

# 3. Count Route
@app.route('/count/<int:num>')
def count(num):
    numbers = "\n".join(str(i) for i in range(num)) + "\n"  # Add newline at the end
    return numbers


# 4. Math Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2  # Use 'div' instead of '/'
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)

if __name__ == "__main__":
    app.run(port=5555)
