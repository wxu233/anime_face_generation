import os
import cv2
from os import listdir
from os.path import isfile, join
import time

onlyfiles = [f for f in listdir('img') if isfile(join('img', f))]


# 特徴量ファイルをもとに分類器を作成
classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')

for name in onlyfiles:
    # 顔の検出
    image = cv2.imread('img/'+name)
    print('try',name)
# グレースケールで処理を高速化
    try:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception:
        continue
    faces = classifier.detectMultiScale(gray_image)

# ディレクトリを作成
    output_dir = 'faces'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (x, y, w, h) in enumerate(faces):
    # 一人ずつ顔を切り抜く
        face_image = image[y:y+h, x:x+w]
        output_path = os.path.join(output_dir, str(i) + name)
        try:
            cv2.imwrite(output_path, face_image)
        except Exception:
            continue
        print('done',name)
while True:
    a = 1
    
    

