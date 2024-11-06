from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    #  Save the uploaded profile picture to the uploads directory. Accept only image files.
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        return 'File uploaded successfully' 
    else:
        return 'Invalid file type'
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def save_document():
    doc = request.files['document']
    #Save the uploaded document to the documents directory.Generate a secure filename and return the save path.
    filename = secure_filename(doc.filename)
    doc.save(os.path.join('documents', filename))
    return f'Document saved at: /documents/{filename}'

def process_image():
    image = request.files['image']
    #Process the uploaded image file: resize it to 100x100 and save it as a thumbnail.
    filename = secure_filename(image.filename)
    image.save(os.path.join('images', filename))
    

if __name__ == '__main__':
    app.run()

# To fix the vulnerability, validate the 'filename' and 'path' parameters to ensure they are safe to use.
# For example, restrict the filenames to a specific directory or whitelist allowed file extensions.

# The code snippet above is vulnerable to CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal').