import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")


args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#this defines the height and width of image
(h, w) = image.shape[:2]
#this defines a center point
center = (w / 2, h / 2)

#this rotates our matrix by 45 degrees
M = cv2.getRotationMatrix2D(center, 45, 5.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)


#this rotates the image by 90 degrees

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 90 degrees", rotated)
cv2.waitKey(0)


rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)
cv2.waitKey(0)