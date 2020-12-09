from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

OUTPUT_FOLDER = './output_images'
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/upload', method=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template("index.html", message="ファイルを指定してください。")

    fs = request.files['file']
    fs.save(UPLOAD_FOLDER + '/' + secure_filename(fs.filename))
    return render_template("index.html", message="ファイルのアップロードが完了しました。")

@app.route('/uploaded_list/')
def uploaded_list():
    files = glob.glob("./images/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))
    return render_template("filelist.html", page_title="アップロードファイル", target_files=urls)


@app.route('/grayscale_list/')
def uprocessed_gs_list():
    pass

@app.route('/canny_list/')
def uprocessed_ca_list():
    pass

@app.route('/face_list/')
def uprocessed_fc_list():
    pass

if __name__ == "__main__":
    app.run(debug=True)

