import os
import shutil

def copy_image(src_path,dst_path):

    print(src_path)
    print(dst_path)
    shutil.copy(src_path, dst_path)
    print('Copied')


def read_file_and_copy(file_path,folder_path,src_path):
    
    file = open(file_path, 'r')
    Lines = file.readlines()
    # Strips the newline character
    for line in Lines:
        img_path = os.path.join(src_path , line.strip() )
        dst_path=folder_path
        copy_image(img_path,dst_path)
   


def create_folder(folder_path):
    
    os.mkdir(folder_path)
    print("done creation")
    




files_path=r"D:\4th year\1 term\graduation project\activity data set\ImageSplits"
dst_path=r"D:\4th year\1 term\graduation project\activity data set\JPEGImages\data"
src_path = r"D:\4th year\1 term\graduation project\activity data set\JPEGImages" 



for file_name in os.listdir(files_path):
    file_path=os.path.join(files_path, file_name )
    folder_path=os.path.join(dst_path,file_name)
    folder_path=folder_path.split(".")[0]
    if os.path.exists(folder_path):
        read_file_and_copy(file_path,folder_path,src_path)
    else:

        create_folder(folder_path)
        read_file_and_copy(file_path,folder_path,src_path)
