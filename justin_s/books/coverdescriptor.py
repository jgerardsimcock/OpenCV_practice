import numpy as np 
import cv2

class CoverDescriptor:
  def __init__(self, kpMethod = "SIFT", descMethod = "SIFT"):
    #store methods for keypoint detection and descriptor
      self.kpMethod = kpMethod
      self.descMethod = descMethod

  def describe(self, image):
    #detect key points in the image
      detector = cv2.FeatureDetector_create(self.kpMethod)
      kps = detector.detect(image)

      #extract local invariant descriptors from key points
      #convert keypoint to a numpy array
      extractor = cv2.DescriptorExtractor_create(self.descMethod)

      (kps, descs) = extractor.compute(image, kps)
      kps = np.float32([kp.pt for kp in kps])
      #return tuple of kps and descriptors
      return (kps, descs)

