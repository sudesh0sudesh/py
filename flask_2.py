from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from mail_flask import mail_details, reader
import os
import email

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'eml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return """
            <!doctype html>
            <head><link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}"></head>
            <title>Submit EML file</title>
            <h1>NO_file_selected/Submit EML file</h1>
            <body style='bgcolor:red;'>
            <form method=post enctype=multipart/form-data>
              <input type=file class=btn btn-primary name=file>
              <input type=submit class="btn btn-primary" value=submit>
            </form>
            </body>
            """
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_read=file.read()
            maile=email.message_from_bytes(file_read)
            output=reader(maile)
            return """
            <!doctype html>
            <head><link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}"></head>
            <title>Submit  EML file</title>
            <h1>Submit Another EML file</h1>
            <body style='bgcolor:red;'>
            <form method=post enctype=multipart/form-data>
              <input type=file class=btn btn-primary name=file>
              <input type=submit class="btn btn-primary" value=submit>
            </form>
            </body>
            """ + output

            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return """
    <!doctype html>
    <head><link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}"></head>
    <title>Submit EML file</title>
    <h1>Submit EML file</h1>
    <body style='bgcolor:red;'>
    <form method=post enctype=multipart/form-data>
      <input type=file class=btn btn-primary name=file>
      <input type=submit class="btn btn-primary" value=submit>
    </form>
    </body>
    """

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


if __name__ == "__main__":
    app.run()
