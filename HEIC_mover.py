import os
from PIL import Image
import shutil
from tqdm import tqdm
import datetime


PIC_PATH = "G:\\Pic_all"  #E:\Pic_all  window
# SAVE_PATH = "G:\\Pic_Sort"
SAVE_PATH = "G:\\Pic_HEIC" #HEIC mode   window

# PIC_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort/pic_raw"  #Mac
# SAVE_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort/save_pic" #Mac


pic_ext_list = [".heic"]

DVICE_LIST = ['Apple', 'SAMSUNG', 'samsung', 'KTH' , 'Snowcorp', 'Canon', 'SONY', 'NIKON CORPORATION', 'Panasonicclear']

pic_file_path_list = []
# file_list = os.listdir(PIC_PATH)
for (root, dirs, files) in os.walk(PIC_PATH):
        # print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                # print("dir: " + dir_name)
                pass

        if len(files) > 0:
            for file_name in files:
                basename, ext =os.path.splitext(file_name)
                if ext.lower() in pic_ext_list:
                    pic_file_path_list.append([root,basename,ext])
                    # print(os.path.join(root,basename+ext)) # debug
                else:
                    print(ext)

for dir, basename, ext in tqdm(pic_file_path_list):
    file_name = basename + ext
    pic_file_path = os.path.join(dir,basename + ext)
    shutil.move(pic_file_path,os.path.join(SAVE_PATH, file_name))
