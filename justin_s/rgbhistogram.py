import numpy as np 
import cv2


class RGBHistogram:
  def __init__(self, bins):
    #store the number of bins for histogram
    self.bins = bins

  def describe(self, image, mask = None):
    #create 3D  histogram in RGB colorspace for each image
    #normalize to reduce the effect of size of image
    #similiar images will have similar histrograms
    hist = cv2.calcHist([image], [0,1,2], 
      mask, self.bins, [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist)

    #return a flattened array 
    return hist.flatten()

