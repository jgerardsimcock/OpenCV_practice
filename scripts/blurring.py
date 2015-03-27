import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#average blurring
average_blurred = np.hstack([
    cv2.blur(image, (1, 1)),
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
    ])

cv2.imshow("Averaged", average_blurred)
#cv2.waitKey(0)

gaussian_blur = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0),
    ])
cv2.imshow("Gaussian", gaussian_blur)
#cv2.waitKey(0)

median_blur  = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7),
    ])
cv2.imshow("Median", median_blur)
#cv2.waitKey(0)

bilateral_blur = np.hstack([
  cv2.bilateralFilter(image, 5, 21, 21),
  cv2.bilateralFilter(image, 7, 31, 31),
  cv2.bilateralFilter(image, 9, 41, 41),
  ])

cv2.imshow("bilateral", bilateral_blur)
cv2.waitKey(0)

