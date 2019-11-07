from PIL import Image
import os

path = r'H:/videos/detection/'
dirs = os.listdir(path)
for dir in dirs:
    dir=path+dir
    print(dir)
    im = Image.open(dir)#返回一个Image对象
    print('宽：%d,高：%d'%(im.size[0],im.size[1]))