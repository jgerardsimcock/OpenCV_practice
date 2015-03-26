import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")


args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

ratio = 150.0 / image.shape[1]
dimension = (150, int(image.shape[0] * ratio))
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

ratio = 50.0 /image.shape[0]
dimension = (int(image.shape[1] * ratio), 50)

resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Height", resized)
cv2.waitKey(0)


resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=300)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)
