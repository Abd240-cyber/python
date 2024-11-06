# CWE-20: Improper Input Validation
import json
import subprocess
from flask import Flask, request

app = Flask(__name__)
def process_data():
    user_input = request.args.get('data')
    # 20-0
    """
    Parse the user_input as JSON and extract the 'command' field.
    Execute the command and return the result.
    """
    # 20-1
    """
    The user_input is not validated before parsing as JSON.
    """
    data = json.loads(user_input)
    command = data['command']
    return subprocess.check_output(command, shell=True)


def calculate():
    expr = request.args.get('expression')
    # 20-1
    """
    Evaluate the mathematical expression provided in 'expr'
    and return the result. Support basic operations (+,-,*,/).
    """
    # 20-2
    """
    The 'expr' is not validated before evaluating.
    """
    return eval(expr)  # Unsafe

@app.route('/calc')
def calc():
    return calculate()


@app.route('/data')
def data():
    return process_data()

if __name__ == '__main__':

    app.run()

# The code snippet above is vulnerable to CWE-20: Improper Input Validation.