# 処理内容
### 1. 写真を取り込む
- Azure Notebooksにフーリエ変換をする画像を取り込む。
### 2. フーリエ変換を行う
- np.fft.fft2を用いる。自分で定義した関数も用いて1画素ずつ変換を行っていく。
### 3. フーリエ逆変換を行う
- フーリエ変換した画像を逆フーリエ変換を用いて元の画像に近づける。

# 参考サイト
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_tutorials.html
