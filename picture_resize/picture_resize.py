# -*- coding: utf-8 -*-

import argparse
from PIL import Image
import os


def resize_picture(name):
    img = Image.open(name)
    global ratio
    w, h = img.size
    print('%s的原始尺寸为：%s×%s' % (name, w, h))
    out_img = img.resize((int(w * ratio), int(h * ratio)))
    out_name = name[:-4] + str(int(w * ratio)) + '×' + \
        str(int(h * ratio)) + name[-4:]
    print('输出的文件路径：', out_name)
    out_img.save(out_name, 'jpeg')


def judge_name(name, reserve='Y'):
    if os.path.isfile(name):
        resize_picture(name)
        if reserve == 'N':
            os.remove(name)
    elif os.path.isdir(name):
        pic_lst = os.listdir(name)
        for i in range(len(pic_lst)):
            path = os.path.join(name, pic_lst[i])
            try:
                resize_picture(path)
                if reserve == 'N':
                    os.remove(path)
            except:
                Exception


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="参数为文件名或目录名")
    arg = parser.parse_args()
    name = arg.path
    ratio = float(input('请输入要压缩图片的比率(例如要压缩50%，请输入0.5):'))
    reserve_file = input('是否保留文件(Y/N)：')
    judge_name(name, reserve_file)
