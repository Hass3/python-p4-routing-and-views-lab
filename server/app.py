#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:message>')
def print_string(message):
    print(message)
    return f'{message}'

@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(i) for i in range(number)) +'\n'
    
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    if operation == "+":
        result = int(num1) + int(num2)
    elif operation == "-":
        result = int(num1) - int(num2)
    elif operation == "*":
        result = int(num1) * int(num2)
    elif operation == "div":
        result = int(num1) / int(num2)
    elif operation == "%":
        result =  int(num1)% int(num2)
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
