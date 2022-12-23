import os
from PIL import Image
import shutil


PIC_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort"
SAVE_PATH = "/Users/hwanju/Desktop/Python workspace/PicSort/save_pic"

pic_ext_list = [".jpg", ".jpeg", ".jpe",".gif" ".png" ]

pic_file_path_list = []
# file_list = os.listdir(PIC_PATH)
for (root, dirs, files) in os.walk(PIC_PATH):
        print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)

        if len(files) > 0:
            for file_name in files:
                basename, ext =os.path.splitext(file_name)
                if ext.lower() in pic_ext_list:
                    pic_file_path_list.append([root,basename,ext])
                else:
                    print("대문자")

for dir, basename, ext in pic_file_path_list:
    file_name = basename + ext
    pic_file_path = os.path.join(dir,basename + ext)
    img = Image.open(pic_file_path)
    meta_data = img._getexif()
    
    try:  # 사진은 월별로 저장
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
        # pass
        none_dir = os.path.join(SAVE_PATH,"None")
        new_path  = os.path.join(none_dir,file_name)
        shutil.move(pic_file_path,new_path)