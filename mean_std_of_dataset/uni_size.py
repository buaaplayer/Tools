from PIL import Image
import os
import cv2 as cv


def image_resize(image_dir, new_dir):  # 统一图片尺寸
    print('============>>修改图片尺寸')
    items=os.listdir(image_dir)
    for img_name in items:
        print('长度:',len(items))
        img_path = os.path.join(image_dir,img_name)  # 获取该图片全称
        # image = Image.open(img_path)  # 打开特定一张图片
        # image = image.resize((512, 512))  # 设置需要转换的图片大小
        img=cv.imread(img_path)
        img=cv.resize(img,(512,512))
        new_path=os.path.join(new_dir,img_name)
        cv.imwrite(new_path,img)
        # process the 1 channel image
        # image.save(new_path + '/' + img_name)
    print("end the processing!")


if __name__ == '__main__':
    print("ready for ::::::::  ")
    ori_path = "F:/data_guowang/train/img"  # 输入图片的文件夹路径
    new_path = 'F:/data_guowang/tem'  # resize之后的文件夹路径
    image_resize(ori_path, new_path)
