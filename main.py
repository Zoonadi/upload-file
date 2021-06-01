import os
from flask import flash, request, redirect, url_for, render_template, send_from_directory
from app import app
from werkzeug.utils import secure_filename

# these are the files that are allowed to be uploaded
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# this function  checks if an extension is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# this function uploads the file and redirects the user to the URL for the uploaded file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully upload')
            return redirect(url_for('download_file', name=filename))
        else:
            flash("'Allowed file types are 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'")
            return redirect(request.url)

# run the code from here
# change your host to match your IP Address - run iconfig in your terminal to get your IP
if __name__ =="__main__":
    app.run(debug=True,host='localhost',port=5000)
