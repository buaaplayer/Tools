import os
import random
from shutil import copyfile,move



def mv(tvt,s_num):
    imgs_for_select = os.listdir(src_path_img_folder)
    select_imgs=random.sample(imgs_for_select,s_num)
    for select_img in select_imgs:
        src_img_path=os.path.join(src_path_img_folder,select_img)
        dst_tvt_img_folder=os.path.join(dst_tvt_folder,'img')
        dst_tvt_label_folder = os.path.join(dst_tvt_folder, 'xml')
        if not os.path.exists(dst_tvt_img_folder):
            os.makedirs(dst_tvt_img_folder)
        if not os.path.exists(dst_tvt_label_folder):
            os.makedirs(dst_tvt_label_folder)
        move(src_img_path,dst_tvt_img_folder)
        label=select_img.split('.')[0]+'.xml'
        src_label_path=os.path.join(src_label_folder,label)
        move(src_label_path,dst_tvt_label_folder)





if __name__ == '__main__':
    src_path_img_folder = 'F:/data_guowang/jueyuanzi/jpg'
    src_label_folder = 'F:/data_guowang/jueyuanzi/xml'
    dst_path_folder = 'F:/data_guowang/'

    imgs = os.listdir(src_path_img_folder)  #为了获取总数
    num = len(imgs)
    test_num = int(0.1 * num)
    val_num = int(0.1 * num)
    tvt_list=['train','val','test']
    for item in tvt_list:
        dst_tvt_folder=os.path.join(dst_path_folder,item)
        if item=='test':
            slected_num=test_num
        elif item=='val':
            slected_num=val_num
        else :
            slected_num=num-val_num-test_num
        mv(item,slected_num)

    print('well done!!!')

