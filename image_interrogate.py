import numpy
import filemanagement as fm

input_file = fm.get_input_file()

image = numpy.loadtxt(input_file)

print(image[0,0])