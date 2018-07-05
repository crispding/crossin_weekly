from PIL import Image
from os import makedirs
from sys import argv


def fill_image(image):
    width, height = image.size
    new_len = max(width, height)

    new_image = Image.new(image.mode, (new_len, new_len), color='white')

    if width > height:
        new_image.paste(image, (0, int((new_len - height) / 2)))
    else:
        new_image.paste(image, (int((new_len - width) / 2), 0))
    return new_image


def cut_image(image, output_dir):
    new_image = fill_image(image)
    width, height = new_image.size
    print('原始的尺寸：', width, height)
    item_width = width // 3
    item_height = height // 3
    makedirs(output_dir, exist_ok=True)

    for i in range(3):
        for j in range(3):
            box = (j * item_width, i * item_height, (j + 1) * item_width,
                   (i + 1) * item_height)
            crop_image = new_image.crop(box)
            crop_image.save(output_dir + '\pic_%d.jpg' % (i * 3 + j))


if __name__ == '__main__':
    img_to_cut = argv[1]
    img = Image.open(img_to_cut)
    output_dir = 'output-' + argv[1].split('.')[0]
    cut_image(img, output_dir)
    print('九宫格图片已保存在“' + output_dir + '”文件夹中。')
