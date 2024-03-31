from flask import render_template, send_file, send_from_directory,Flask, flash, redirect,request
import os
from werkzeug.utils import secure_filename
import torch
torch.set_num_threads(1)


app = Flask(__name__)

ALLOWED_EXTENSIONS = {'mid'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = 'Allegro-Music-Transformer/Uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("first1_test3.html")

@app.route('/compose', methods=['GET', 'POST'])
def compose_1():
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
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

    return render_template("first.html")

if __name__ == '__main__':
    app.run(debug=True)