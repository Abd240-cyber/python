import os
from flask import request, send_from_directory

def get_file():
    filename = request.args.get('filename')
    #Read and return the contents of the file with the given filename from the uploads directory.
    with open(f'uploads/{filename}', 'r') as file:
        return file.read()

def serve_file():
    path = request.args.get('path')
    #Serve the file from the specified path within the static files directory.
    return send_from_directory('static', path)

if __name__ == '__main__':
    print(get_file())
    print(serve_file())
# To fix the vulnerability, validate the 'filename' and 'path' parameters to ensure they are safe to use.
# For example, restrict the filenames to a specific directory or whitelist allowed file extensions.
# Similarly, validate the 'path' parameter to prevent directory traversal attacks.
# By validating the input, you can prevent attackers from accessing sensitive files or directories on the server.
# The same principle applies to other file-related operations in web applications.

