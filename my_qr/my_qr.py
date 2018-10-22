# -*- coding: utf-8 -*-

import sys
import os
import qrcode
import zxing
from random import random


def qr_encode(text):
    ran = int(random() * 100000)
    filename = 'qr_output{}.jpg'.format(ran)
    img = qrcode.make(text)
    img.save(filename)
    # img.show()
    print('二维码图片已生成，图片文件在 {}'.format(os.path.abspath(filename)))


def qr_decode(file_name):
    reader = zxing.BarCodeReader()
    msg = reader.decode(file_name).parsed
    print(msg)
    print("{} 中包含信息：{}".format(file_name, msg))


def act():
    args = sys.argv
    if len(args) != 3:
        print("输入错误")
    elif args[1] == 'encode':
        input_text = args[2]
        qr_encode(input_text)
    elif args[1] == 'decode':
        file_path = args[2]
        qr_decode(file_path)


if __name__ == '__main__':
    act()
