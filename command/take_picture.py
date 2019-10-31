# 写真を撮る
# 画像を綺麗にする
#!/usr/local/bin/python3
import cv2
import os
import time
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

target = Path("picture.jpg").touch()
path = os.getcwd()


def picture():
    key = key_action()
    if(key == True):
        # device number
        cap = cv2.VideoCapture(0)
        val_bool, frame = cap.read()
        cv2.imwrite(path + "/picture.jpg", frame)
    else:
        pass
    reading()


def reading():
    x = os.path.exists("./picture.jpg")
    I = cv2.imread("./picture.jpg")
    if(x == True):
        plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
        plt.show()
    else:
        pass


def key_action():
    key = input()
    start = None
    if(key == "p"):
        start = True
        return start
    else:
        start = False
        return start


def correct():
    I = cv2.imread("./picture.jpg")
    gamma = 1.0
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    # Look up tableを使って画像の輝度値を変更
    imgA = cv2.LUT(I, lookUpTable)
    cv2.imwrite(path + "/picture.jpg", imgA)
    reading()


def main():
    count = 0
    while True:
        if(count == 1):
            break
        picture()
        count = count + 1
    correct()
main()
