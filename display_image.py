import numpy
from PIL import Image

with open (r"C:/Users/adam/Desktop/Q13 OLE New Data/Second Try/OLE/IB +BG SUB extra BG added/118.txt", 'r') as f:
    array = numpy.loadtxt(f)

array = array/array.max()*255

img = Image.fromarray(array, 'L')
img.show()