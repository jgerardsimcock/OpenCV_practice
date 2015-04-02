from hog import HOG 
import dataset
import argparse
import cPickle
import mahotas
import cv2

# this allows us to call our program from command line
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required = True,
  help = "path to the model file")
ap.add_argument("-i", "--image", required = True,
  help = "path to where the images file")
args = vars(ap.parse_args())

#load the model from the pickle file
model = open(args["model"]).read()
model = cPickle.loads(model)

#initialize the HOG descriptor

hog = HOG(orientation = 18, pixelsPerCell = (10,10),
    cellsPerBlock = (1,1), normalize = True)

#load image and convert to greyscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.BGR2GRAY)

#blurr image, find edges, find contours on edge regions
blurred = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(blurred, 30, 150)

(cnts, _) = cv2.findContours(edged.copy(), 
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

#sort contours by x axis position so that we are reading from left to right
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])

#loop over contours

for (c, _) in cnts:
  #compute the bounding box in the rectangle
  (x, y, w, h) = cv2.boundingRect(c)
  #if width is greater than 7 pixels and height greater than 20
  # the contour is likely a digit
  if w >= 7 and h >= 20:
    #crop the ROI and then threshold the gray scale
    #ROI will reveal the digit

    roi = gray [y:y + h, x: x + w]
    thresh = roi.copy()
    T = mahotas.thresholding.otsu(roi)
    thresh[thresh > T ] = 255
    thresh = cv2.bitwise_not(thresh)

    #deskey the image, center its extent
    thresh = dataset.deskew(thresh, 20)
    thresh = dataset.center_extent(thresh, (20,20))

    cv2.imshow("thresh", thresh)

    #extract features from image and show it
    hist = hog.describe(thresh)
    digit = model.predict(hog)
    print "This number should be %d" % (digit)

    #draw a rectangle around the digit and then show 
    #what we classified the image as

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.putText(image, str(digit), (x-10), (y-10), 
      cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    cv2.imshow("image", image)
    cv2.waitKey(0)








