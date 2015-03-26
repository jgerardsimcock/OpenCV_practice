import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")


args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flipped = cv2.flip(image,1)
cv2.imshow("Image flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Image flipped horizontally and vertically", flipped)
cv2.waitKey(0)


flipped = cv2.flip(image, 0)
cv2.imshow("Image flipped vertically", flipped)
cv2.waitKey(0)
