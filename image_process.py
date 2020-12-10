from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


import os
import time

import cv2
import numpy as np

# 監視対象ディレクトリを指定する
target_dir = 'images'

def chage_image(filename):

    # # 入力画像を読み込み
    img = cv2.imread(f'images/{filename}')

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f'images/imageoutput_gray/gray_{filename}', gray)

    # # 方法2(OpenCVで実装)
    dst = cv2.Canny(gray, 100, 200)

    cv2.imwrite(f'images/outputimage_canny/canny_{filename}', dst)

    

    th, niti_th = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    cv2.imwrite(f'images/outputimage_threshold/threshold_{filename}', niti_th)

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):
     # ファイル作成時のイベント
     def on_created(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s created' % filename)
         if(filename != '.DS_Store' and filename != 'images'):
            chage_image(filename)

     # ファイル変更時のイベント
     def on_modified(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s changed' % filename)
         if(filename != '.DS_Store' and filename != 'images'):
            chage_image(filename)


# コマンド実行の確認
if __name__ == "__main__":
     # ファイル監視の開始
     event_handler = FileChangeHandler()
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     # 処理が終了しないようスリープを挟んで無限ループ
     try:
         while True:
             time.sleep(0.1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()





