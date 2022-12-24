import os
from PIL import Image
import shutil
from tqdm import tqdm
import datetime


PIC_PATH = "G:\\Pic_all"  #E:\Pic_all window
SAVE_PATH = "G:\\Pic_HEIC" #HEIC mode window

# PIC_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort/pic_raw" # Mac
# SAVE_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort/save_pic" # Mac

pic_ext_list = [".jpg", ".jpeg", ".jpe",".gif", ".png", ".bmp" ]
# pic_ext_list = [".zip" ] # debug
# pic_ext_list = [".heic"]

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
                    pass


        if len(files) == 0 and len(dirs) == 0:
            print(root)
            shutil.rmtree(root)

for dir, basename, ext in tqdm(pic_file_path_list):
    file_name = basename + ext
    pic_file_path = os.path.join(dir,basename + ext)
    img = Image.open(pic_file_path)
    meta_data = img.getexif()
    # print(meta_data)
    


    try:  # 사진은 월별로 저장
        if meta_data[271] in DVICE_LIST:
            make_time = meta_data[306]
        
        else:
            make_time = meta_data[36867]
        year = make_time[0:4]
        month = make_time[5:7]
        day = make_time[8:10]

        new_name = make_time.replace(":","_")
        
        year_dir = os.path.join(SAVE_PATH,year)
        month_dir = os.path.join(year_dir,month)


        if os.path.exists(year_dir):
            pass
        else:
            os.mkdir(year_dir)
        
        if os.path.exists(month_dir):
            pass
        else:
            os.mkdir(month_dir)
        
        cnt = 0 
        new_path  = os.path.join(month_dir,new_name + "_(" + str(cnt) + ")" + ext)
        while os.path.exists(new_path):
            cnt += 1
            new_path  = os.path.join(month_dir,new_name + "_(" + str(cnt) + ")" + ext)
        
        shutil.move(pic_file_path,new_path)

        

        

    except: # None 폴더로 모이도록 조정

        img.close()

        # pass
        ctime = os.path.getctime(pic_file_path)
        rtime = datetime.datetime.fromtimestamp(ctime).strftime("%Y_%m_%d %H_%M_%S")

        year = rtime[0:4]
        month = rtime[5:7]

        year_dir = os.path.join(SAVE_PATH,year)
        month_dir = os.path.join(year_dir,month)

        if os.path.exists(year_dir):
            pass
        else:
            os.mkdir(year_dir)
        
        if os.path.exists(month_dir):
            pass
        else:
            os.mkdir(month_dir)

        
        cnt = 0
        new_path  = os.path.join(month_dir,rtime + "_(" + str(cnt) + ")" + ext)
        while os.path.exists(new_path):
            cnt += 1
            new_path  = os.path.join(month_dir,rtime + "_(" + str(cnt) + ")" + ext)

        # none_dir = os.path.join(SAVE_PATH,"None")
        # print(meta_data)
        # new_path  = os.path.join(none_dir,file_name)
        shutil.move(pic_file_path,new_path)