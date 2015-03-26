import numpy as np
import cv2

canvas = np.zeros((400,400,3), dtype="uint8")


# green = (0, 255, 0)
# cv2.line(canvas, (0, 0), (300, 300), green)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# red = (0, 0, 255)
# cv2.line(canvas, (300, 0), (0, 300), red, 3)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# cv2.rectangle(canvas, (10,10), (60,60), green)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# cv2.rectangle(canvas, (50,200), (200,225), red, 5)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# blue = (255, 0, 0)
# cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

#Lets draw circles
# (centerX, centerY) = (canvas.shape[1] / 2 , canvas.shape[0] / 2)
# white = (255, 255, 255)

# for  r in xrange(0, 175, 5):
#   cv2.circle(canvas, (centerX, centerY), r, white)

# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

#Now let's randomly draw circles of various colors

for i in xrange(0, 25):
  #this makes a radius of a random value
  radius = np.random.randint(5, high=150)
  #this makes a RGB color from random value
  color = np.random.randint(0, high = 255, size = (3,)).tolist()
  #this creates a tuple of size two that we use as our center
  pt = np.random.randint(0, high=300, size=(2,))
  #we then create a circle with those values
  cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

