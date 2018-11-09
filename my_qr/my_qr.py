# -*- coding: utf-8 -*-

import sys
import os
import qrcode
import zxing
from random import random
import argparse


def qr_encode(text):
    ran = int(random() * 100000)
    filename = 'qr_output{}.jpg'.format(ran)
    img = qrcode.make(text)
    img.save(filename)
    # img.show()
    print('二维码图片已生成，图片文件在 {}'.format(os.path.abspath(filename)))


def qr_decode(file_name):
    reader = zxing.BarCodeReader()
    msg = reader.decode(file_name).raw
    print("{} 中包含信息：{}".format(file_name, msg))


def act():
    parser = argparse.ArgumentParser(description="生成或读取二维码")
    parser.add_argument(
        "operation",
        choices=['encode', 'decode'],
        help="请选择 ‘decode’ 或者 'encode'")
    parser.add_argument("content")
    args = parser.parse_args()
    if args.operation == 'encode':
        qr_encode(args.content)
    else:
        try:
            qr_decode(args.content)
        except IOError:
            print("请输入正确的二维码")


if __name__ == '__main__':
    act()
