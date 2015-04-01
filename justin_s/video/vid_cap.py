import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)



fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret==True:
        frame = cv.flip(frame, 0)

        out.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
          break
    else: 
        break


cap.release()
out.release()
cv.destroyAllWindows()




#this is just to access camera
# while(True):

#   #capture frame by frame
#   ret, frame = cap.read()

#   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#   cv.imshow('frame', gray)
#   if cv.waitKey(1) & 0xFF == ord('q'):
#       break

# cap.release()
# cv.destroyAllWindows()