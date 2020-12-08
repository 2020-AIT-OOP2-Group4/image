from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

UPLOAD_FOLDER = './upload_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

OUTPUT_FOLDER = './output_images'
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/upload' method=['POST'])
def upload():
    fs = request.files['file']
    fs.save(UPLOAD_FOLDER + '/' + secure_filename(fs.filename))
    return render_template("index.html", message="ファイルのアップロードが完了しました。")

@app.route('')
def uploaded_list():
    pass


if __name__ == "__main__":
    app.run(debug=True)

