import os
from PIL import Image
import shutil
from tqdm import tqdm
import datetime


VOD_PATH = "G:\\Pic_all"  #E:\Pic_all
# SAVE_PATH = "G:\\Pic_Sort"
SAVE_PATH = "G:\\video" #HEIC mode

# pic_ext_list = [".jpg", ".jpeg", ".jpe",".gif", ".png", ".bmp" ]
VOD_ext_list = [".mkv", ".avi" ,".mp4" ,".mpg" ,".flv" ,".wmv" ,".asf" ,".asx",".ogm", ".ogv",".mov",".aae",".3gp",".dat"]
# pic_ext_list = [".zip" ] # debug
# pic_ext_list = [".heic"]

DVICE_LIST = ['Apple', 'SAMSUNG', 'samsung', 'KTH' , 'Snowcorp', 'Canon', 'SONY', 'NIKON CORPORATION', 'Panasonicclear']

vod_file_path_list = []
# file_list = os.listdir(VOD_PATH)
for (root, dirs, files) in os.walk(VOD_PATH):
        # print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                # print("dir: " + dir_name)
                pass

        if len(files) > 0:
            for file_name in files:
                basename, ext =os.path.splitext(file_name)
                if ext.lower() in VOD_ext_list:
                    vod_file_path_list.append([root,basename,ext])
                    # print(os.path.join(root,basename+ext)) # debug
                else:
                    print(os.path.join(root,basename+ext))
                    pass


        if len(files) == 0 and len(dirs) == 0:
            print(root)
            shutil.rmtree(root)

for root, basename, ext in tqdm(vod_file_path_list):
    file_name = basename + ext
    vod_file_path = os.path.join(root, basename + ext)
    

    ext_path = os.path.join(SAVE_PATH,ext.upper()[1:4])

    if not os.path.exists(ext_path):
        os.mkdir(ext_path)

    new_vod_path = os.path.join(ext_path,file_name)

    shutil.move(vod_file_path, ext_path)

    