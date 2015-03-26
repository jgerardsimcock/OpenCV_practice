import cv2
import numpy as np

def translate(image, x, y):
  Matrix = np.float([[1,0, x], [0, 1, y]])
  shifted = cv2.warpAffine(image, Matrix, (image.shape[1], image.shape[0]))

  return shifted


def rotate(image, angle, center=None, scale=1.0):

  #set a variable equal to dimension of shape 
  (h, w) = image.shape[:2]

  if center is None:
    center = (w / 2, h / 2)

  Matrix = cv2getRotationMatrix2D(center, angle, scale)
  rotated = cv2.warpAffine(image, Matrix, (w, h))

  return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
  dimension = None
  
  (h,w) = image.shape[:2]

  if width is None and height is None:
    return image

  if width is None:
    ratio = height / float(h)
    dimension = (int(w * ratio), height)

  else: 
    ratio = width / float(w)
    dimension = (width, int(h*ratio))

  resized = cv2.resize(image, dimension, interpolation = inter)

  return resized





