import rgbhistogram
from sklearn.prepocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import numpy as np 
import argparse
import glob
import cv2


#arguments to parse
#this time we are parsing the images and the masks
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True,
  help = "path to the image dataset")
ap.add_argument("-m", "--masks", required = True,
  help = "path to the image masks")
args = vars(ap.parse_args())

#we need to sort and do io for the images and masks  
imagePaths = sorted(glob.glob(args["images"] + "/*.png"))
maskPaths = sorted(glob.glob(args["masks"] + "/*.png"))

#initialize the lists where we will store data and labels

data = []
target = []

#initialize the image descriptor
desc = RGBHistogram([8,8,8])

#this loops over the list of images and masks
for (imagePath, maskPath) in zip(imagePaths, maskPaths):
  #load the image and masks 

  image = cv2.imread(imagePath)
  mask = cv2.imread(maskPath)

  mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

  #describe the image according to its feature set
  features = desc.describe(image, mask)

  #append each image/mask combo to list of data
  data.append(features)
  target.append(imagePath.split("_")[-2])


#create a list of unique target names
targetNames = np.unique(target)
#instantiate encoder
le = LabelEncoder()
#fit and transform 
target = le.fit_transform(target)

#create train/test split 
(trainData, testData, trainTarget, testTarget) = train_test_split(data, target
    test_size = 0.3, random_state = 42)

#train the classifier/model
model = RandomForestClassifier()
model.fit(trainData, trainTarget)

#evaluate the classifier
print classification_report(testTarget, model.predict(testData)
    target_names = targetNames)

#get a random sample of images
for i in np.random.choice(np.arange(0, len(imagePaths)), 10):

  #get image and mask paths
  imagePath = imagePaths[i]
  maskPath = makspaths[i]


  #load the image and mask 

  image = cv2.imread(imagePath)
  mask = cv2.imread(maskPath)
  mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

  features = desc.describe(image, mask)

  #predict what type flower the image is

  flower = le.inverse_transform(model.predict(features))[0]
  print imagePath
  print "I think this flower is %s" % (flower.upper)
  cv2.imshow("image", image)
  cv2.waitKey(0)




