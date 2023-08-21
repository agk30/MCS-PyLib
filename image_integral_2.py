import os
import filemanagement as fm
import numpy
import roi

input_folder = fm.get_input_folder()

bg_image_path = fm.get_input_file()

#[top, left, bottom, right]
rect_roi = [270, 285, 510, 475]

summed_list =[]

with open(bg_image_path, 'r') as f:
    bg_image = numpy.loadtxt(f)
for root, dirs, files in os.walk(input_folder):
    for file in files:
        with open(os.path.join(root, file), 'r') as g:
            image = numpy.loadtxt(g)
            image = image - bg_image
            sum_slice = roi.rect_sum(rect_roi, image)
            summed_list.append(sum_slice)

print (summed_list)
