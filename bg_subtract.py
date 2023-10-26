import numpy    
import filemanagement as fm
import os

bg_image = numpy.loadtxt(r"C:\Users\adam\Desktop\Q13 OLE New Data\Second Try\10_08_2023_13_36_is_Q13_PFPE__bg\0.txt")
input_folder = fm.get_input_folder()
output_folder = "subtracted images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for root, dirs, files in os.walk(input_folder):
    for file in files:
        with open(root+"/"+file,'r') as f:
            image = numpy.loadtxt(root+"/"+file)
            #print(image.shape, bg_image.shape, root+"/"+file)
            try:
                sub_image = image - bg_image
                with open(output_folder+"/"+file,'w') as g:
                    numpy.savetxt(g, sub_image)
            except:
                print("error in", root+"/"+file)

print("おわり！")
