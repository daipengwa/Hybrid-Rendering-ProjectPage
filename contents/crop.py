import cv2, glob
import numpy as np

names = glob.glob('./point_nerf/*.png')

for i in range(len(names)):
    name =  names[i]
    img = cv2.imread(name)
    cv2.imwrite(name, img[20:-20, 20:-20, :])