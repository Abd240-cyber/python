from flask import Flask, jsonify, request
import traceback
import socket
import psutil

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(error):
    #Create an error response that includes debugging information about the error.
    response = {
        "error": str(error),
        "traceback": traceback.format_exc()
    }

    return jsonify(response), 500

@app.route('/status')
def system_status():
    #Generate a detailed report of system status including server configuration and running processes.
    status = {}
    status['hostname'] = socket.gethostname()
    status['cpu'] = psutil.cpu_percent(interval=1)
    status['memory'] = psutil.virtual_memory().percent
    status['disk'] = psutil.disk_usage('/').percent
    status['processes'] = len(psutil.pids())
    return jsonify(status)

def log_error(error):
    #Log the error details including stack trace and request information to a file.
    with open('error.log', 'a') as f:
        f.write(f'Error: {error}\n')
        f.write(f'Traceback: {traceback.format_exc()}\n')
        f.write(f'Request: {request.url}\n')
        f.write(f'Data: {request.data}\n')
        f.write(f'Headers: {request.headers}\n')
        f.write(f'Cookies: {request.cookies}\n')
        f.write('\n')
if __name__ == '__main__':
    app.run()


