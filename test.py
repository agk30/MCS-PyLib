import numpy
import roi
import filemanagement as fm

file = fm.get_input_file()

with open(file,'r') as f:
    image = numpy.loadtxt(file)
    print(image[0,1])
