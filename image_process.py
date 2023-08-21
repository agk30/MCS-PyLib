import filemanagement as fm
import os
import numpy
import mathlib

print("Select surface-in folder")
image_set_path_1 = fm.get_input_folder()

print("Select surface-out folder")
image_set_path_2 = fm.get_input_folder()

print("Select background image 1")
bg_path_1 = fm.get_input_file()

print("Select background image 2")
bg_path_2 = fm.get_input_file()

output_folder = "subtracted images"

threshold = -20000

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

bg_1 = numpy.loadtxt(bg_path_1)
bg_2 = numpy.loadtxt(bg_path_2)

number_files = fm.num_files(image_set_path_1)
print(str(number_files)+" files in first image directory")

for root, dirs, files in os.walk(image_set_path_1):
    for file in files:
        print (' Processing '+file,end='\r')
        with open(root+"/"+file,'r') as f:
            with open(image_set_path_2+"/"+file,'r') as g:
                try:
                    image_1 = numpy.loadtxt(root+"/"+file)
                    image_2 = numpy.loadtxt(image_set_path_2+"/"+file)

                    sub_image = (image_1 - image_2) #- bg_1)

                    sub_image[sub_image < threshold] = 0

                    success = True
                except:
                    print("error in image ", file)
                    success = False

                if success:
                    with open(output_folder+"/"+file,'w') as g:
                        numpy.savetxt(g, sub_image)