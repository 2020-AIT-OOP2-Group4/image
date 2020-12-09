#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import random
from flask import Flask, request, render_template, Blueprint

app = Flask(__name__)

#静的ディレクトリの追加
add_app = Blueprint("images", __name__, static_url_path="/images", static_folder="./images")
app.register_blueprint(add_app)

@app.route('/')
def image_out():

    path = "./images"
    
    files = os.listdir(path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    print(files_file)   # ['file1', 'file2.txt', 'file3.jpg']

    return render_template ('filelist.html', files_file = files_file)

# 画像を出力
# print "Content-Type: image/jpeg"
# print "Content-Length: %d\n" % os.stat(img_src).st_size
# print open(img_src,"rb").read()

if __name__ == '__main__':
    app.run()
    debug = True