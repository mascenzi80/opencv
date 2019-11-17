import matplotlib
matplotlib.rcParms['figure.figsize']=(6.0, 6.0)
matplotlib.rcParms['image.cmap']='gray'

import cv2
import numpy as numpy
from dataPath import DATA_PATH
import matplotlib.pyplot as pyplot
%matplotlib inline

imagePath = DATA_PATH + "/images/number_zero.jpg"

#  Read image in Grayscale format
testImage = cv2.imread(imagePath, 0)
print(testImage)