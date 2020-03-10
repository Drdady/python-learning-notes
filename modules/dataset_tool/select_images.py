# -*-coding: utf-8 -*-
"""
    @Project: python-learning-notes
    @File   : select_images.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-09-23 16:04:20
"""

import os
import numpy as np
import shutil
import os.path
from utils import file_processing, image_processing


def ramdom_select_image_dir(image_dir, dest_dir):
    select_nums = 100
    image_id = file_processing.get_sub_directory_list(image_dir)
    for id in image_id:
        image_list = file_processing.get_files_list(os.path.join(image_dir, id),
                                                    postfix=['*.jpg', "*.jpeg", '*.png', "*.JPG"])
        image_list = np.random.permutation(image_list)[:select_nums]
        for src_path in image_list:
            basename = os.path.basename(src_path)
            dest_path = file_processing.create_dir(dest_dir, id, basename)
            shutil.copy(src_path, dest_path)


def select_image_dir(image_dir, dest_dir):
    image_id = file_processing.get_sub_directory_list(image_dir)
    for id in image_id:
        image_list = file_processing.get_files_list(os.path.join(image_dir, id),
                                                    postfix=['*.jpg', "*.jpeg", '*.png', "*.bmp"])
        for src_path in image_list:
            basename = os.path.basename(src_path)
            index = basename.split(".")[0].split("_")[1]
            if index=="0":
                dest_path = file_processing.create_dir(dest_dir, id, basename)
                # shutil.copy(src_path, dest_path)
                file_processing.move_file(src_path, dest_path)


if __name__ == "__main__":
    # image_dir = '/media/dm/dm1/FaceDataset/lexue/lexue1/val-src'
    # dest_dir = '/media/dm/dm1/FaceDataset/lexue/lexue1/val'
    # ramdom_select_image_dir(image_dir, dest_dir)

    image_dir = '/media/dm/dm1/FaceDataset/X4/CASIA-FaceV5/trainval'
    dest_dir = '/media/dm/dm1/FaceDataset/X4/CASIA-FaceV5/facebank'
    select_image_dir(image_dir, dest_dir)