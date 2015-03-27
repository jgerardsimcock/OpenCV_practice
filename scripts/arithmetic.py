import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")


args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#two types of arithmetic: opencv and numpy
 

print "OpenCV max of 255: " + str(cv2.add(np.uint8([200]), np.uint8
([100])))


print "OpenCV min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8
([100])))

print "Numpy wrap around: " + str(np.uint8([200]) + np.uint8([100]))

print "Numpy wrap around: " + str(np.uint8([50]) - np.uint8([100]))

#we create a matrix with values of 100
Matrix = np.ones(image.shape, dtype="uint8") * 100
#we then add that matrix to our image to make it brighter
added = cv2.add(image, Matrix)
cv2.imshow("Added", added)

#we create a matrix with values of 50
Matrix = np.ones(image.shape, dtype = "uint8") * 50
#we then add our matrix to the image matrix
subtracted = cv2.subtract(image, Matrix)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)