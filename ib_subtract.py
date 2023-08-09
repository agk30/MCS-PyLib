import numpy    
import filemanagement as fm
import os

print("Select surface-in folder")
surface_in_folder = fm.get_input_folder()
print("Select surface-out folder")
surface_out_folder = fm.get_input_folder()
output_folder = "subtracted images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for root, dirs, files in os.walk(surface_in_folder):
    for file in files:
        print (' Processing '+file,end='\r')
        with open(root+"/"+file,'r') as f:
            try:
                surface_in_image = numpy.loadtxt(root+"/"+file)
                surface_out_image = numpy.loadtxt(surface_out_folder+"/"+file)
                sub_image = surface_in_image - surface_out_image
                success = True
            except:
                print("error in image ", file)
                success = False

            if success:
                with open(output_folder+"/"+file,'w') as g:
                    numpy.savetxt(g, sub_image)
