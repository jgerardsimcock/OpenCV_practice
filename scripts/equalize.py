import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")


args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#this is the line of code that equalizes the histogram
eq =cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.vstack([image,eq]))
cv2.waitKey(0)
