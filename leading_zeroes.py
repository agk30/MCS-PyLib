import filemanagement as fm
import os

input_folder = fm.get_input_folder()
for root, dirs, files, in os.walk(input_folder):
    for file in files:
        #print(os.path.splitext(file))
        reduced_file = os.path.splitext(file)[0]
        if len(reduced_file) < 3:
            print(reduced_file.zfill(3))
            os.rename(root+"/"+file, root+"/"+reduced_file.zfill(3)+".txt")