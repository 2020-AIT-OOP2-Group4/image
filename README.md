# image
## システムの動作確認方法
1. ターミナルでimage_process.pyのプログラムを動作させる(watchdog)
2. 次にweb.pyを実行する(サーバー)
3. webで上記のサーバーに移動し、画像をuploadする。
4. uploadを行ったら、ターミナル上でimage_process.pyが動いているかを確認する。
5. upload_imagesフォルダに画像処理された画像があるかを確認する。
6. webにあるリンクからグレースケールまたは顔検出のページに飛び、結果が出力されているかを確認する。
## 使用するliblaryのversion
- Flask         1.1.2
- watchdog      0.10.4
- pip           20.1.1
- numpy         1.19.3
