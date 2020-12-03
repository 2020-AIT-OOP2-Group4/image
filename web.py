from flask import Flask, request, render_template
import random 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload' method="post")
def upload():
    fs = request.files['file']
    fs.save(UPLOAD_FOLDER + '/' + secure_filename(fs.filename))
    return render_template("index.html")

@app.route('')
def uploaded_list():
    pass


if __name__ == "__main__":
    app.run(debug=True)

