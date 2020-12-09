from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

OUTPUT_FOLDER_GRAY = './imageoutput_gray'
app.config['OUTPUT_FOLDER_GRAY'] = OUTPUT_FOLDER_GRAY

OUTPUT_FOLDER_FACE = './imageoutput_filta'
app.config['OUTPUT_FOLDER_FACE'] = OUTPUT_FOLDER_FACE

OUTPUT_FOLDER_THRESHOLD = './imageoutput_threshold'
app.config['OUTPUT_FOLDER_THRESHOLD'] = OUTPUT_FOLDER_THRESHOLD

OUTPUT_FOLDER_CANNY = './imageoutput_canny'
app.config['OUTPUT_FOLDER_CANNY'] = OUTPUT_FOLDER_CANNY


@app.route('/')
def index():
    return render_template("index.html", message=None)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template("index.html", message="ファイルを指定してください。")

    fs = request.files['file']


    # ファイルを保存
    fs.save(UPLOAD_FOLDER + '/' + secure_filename(fs.filename))

    return render_template("index.html", message="ファイルのアップロードが完了しました。")


@app.route('/uploaded_list/')
def uploaded_list():
    files = glob.glob("./upload_images/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))
    return render_template("filelist.html", page_title="アップロードファイル", target_files=urls)


@app.route('/grayscale_list/')
def processed_gs_list():
    files = glob.glob("./images/imageoutput_gray/*")
    urls = []
    for file in files:
        urls.append("/processed/gs/" + os.path.basename(file))
    return render_template("filelist.html", page_title="グレースケール", target_files=urls)

@app.route('/threshold_list/')
def processed_ts_list():
    files = glob.glob("./images/imageoutput_threshold/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))
    return render_template("filelist.html", page_title="二値化", target_files=urls)

@app.route('/canny_list/')
def processed_cn_list():
    files = glob.glob("./images/imageoutput_canny/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))
    return render_template("filelist.html", page_title="Canny", target_files=urls)

@app.route('/face_list/')
def processed_face_list():
    files = glob.glob("./images/imageoutput_filta/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))
    return render_template("filelist.html", page_title="顔検出", target_files=urls)


@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/processed/gs/<path:filename>')
def processed_gs_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER_GRAY'], filename)

@app.route('/processed/ts/<path:filename>')
def processed_ts_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER_THRESHOLD'], filename)

@app.route('/processed/cn/<path:filename>')
def processed_cn_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER_CANNY'], filename)

@app.route('/processed/face/<path:filename>')
def processed_face_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER_FACE'], filename)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)