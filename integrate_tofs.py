import numpy
import filemanagement as fm
import os

folder_path =  fm.get_input_folder()

output_filename = "integral.csv"

if os.path.isfile(folder_path+"/"+output_filename):
    os.remove(folder_path+"/"+output_filename)

for root, dirs, files in os.walk(folder_path):

    print("looking in " + root+ "...")

    integral_array = numpy.zeros(((len(files)-1),8))

    print("Gonna go with " + str(len(files)) + " files")

    i = 0
    for file in files:
        file_str = os.path.splitext(file)
        if "wedge" in file_str[0]:
            angle = float(file_str[0].split(" ")[1])
            integral_array[i,0] = angle
            with open(root+"/"+file, 'r') as f:
                array = numpy.loadtxt(f, delimiter = ",")
                for j in range(7):
                    integral = numpy.trapz(y=array[:,j+1], x=array[:,0], axis = 0)
                    integral_array[i,j+1] = integral
            i += 1

# sorts list by angle (should be first column)
new_list =  sorted(integral_array, key=lambda x: x[0])

numpy.savetxt(folder_path+"/"+"integral.csv", new_list, delimiter = ",")

print("Done, I guess, idk, check it yourself")