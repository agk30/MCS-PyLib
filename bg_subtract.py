import numpy    
import filemanagement as fm
import os

bg_image = numpy.loadtxt("C:/Users/adam/Desktop/0.txt")
input_folder = fm.get_input_folder()
output_folder = "subtracted images"
for root, dirs, files in os.walk(input_folder):
    for file in files:
        with open(root+"/"+file,'r') as f:
            image = numpy.loadtxt(root+"/"+file)
            #print(image.shape, bg_image.shape, root+"/"+file)
            sub_image = image - bg_image

            for i in range(800):
                for j in range(800):
                    if image[i,j] < -1000:
                        print("value less than 10,000 in", root+"/"+file)
                        image[i,j] = -1000
            with open(file,'w') as g:
                numpy.savetxt(g, sub_image)
