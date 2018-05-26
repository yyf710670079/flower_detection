#   _*_ coding:utf-8 _*_
__author__ = 'yangyufeng'

"""
PIL数据扩充，翻转、颜色增强等
"""

from PIL.ImageOps import mirror
from PIL import Image
import os

flowers_dir = os.getcwd() + "/flowers_augmentation/"

imgFolds = ['daisy', 'rose', 'sunflower', 'tulip']

for imgFold in imgFolds:

    imgs = os.listdir(flowers_dir + '/' + imgFold)
    imgNum = len(imgs)
    for i in range(imgNum):
        if imgs[i] == ".DS_Store":
            continue
        im_path = flowers_dir + '/' + imgFold + '/' + imgs[i]
        im = Image.open(im_path)
        new_im = mirror(im)
        new_im.save("new_" + imgs[i])







