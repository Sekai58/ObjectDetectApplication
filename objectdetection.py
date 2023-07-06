# Import libraries
import cv2
import numpy as np
import cvlib as cv
from PIL import Image
from cvlib.object_detection import draw_bbox

# Read images
img = Image.open('R.jpg')
img = np.array(img)

# Find the cordinates of the box
bbox, label, conf = cv.detect_common_objects(img, model='yolov3')
print(label,bbox,conf)
output_image = draw_bbox(img, bbox, label, conf)

