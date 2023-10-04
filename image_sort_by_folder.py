import filemanagement as fm
import os
import numpy
import roi

input_folder = fm.get_input_folder()
#input_folder = "test_root/test_folder_123/1.txt"

first_run = True
for root, dirs, files in os.walk(input_folder):
    if first_run:
        total_images = len(dirs)
        print(total_images)
        master_array = numpy.zeros((800,800,total_images))
        print(master_array.shape)
        first_run = False
    
    for file in files:
        partition = root.rpartition("_")
        image_index = int(partition[2])
        print("Loading image ",image_index,end="\r")
        image = numpy.loadtxt(root+"/"+file)
        master_array[:,:,image_index-1] = image

#numpy.save("master_array.npy", master_array)

sum_array = numpy.zeros((total_images,2))

rect_roi = [270, 155, 510, 535]

for i in range(total_images):
    sum_slice = roi.rect_sum(rect_roi, master_array[:,:,i])
    sum_array[i,:] = [i+1, sum_slice]

numpy.savetxt("sum_array.txt", sum_array)