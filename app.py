from flask import Flask
import os

# this is where you will be uploading the file to. You might need to change this to match your path and where you place
# the the upload-file-tutorial folder
path = os.getcwd()
UPLOAD_FOLDER = path + '\\uploads'

app = Flask(__name__)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
