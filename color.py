import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

cap.set(3,320) # Width
cap.set(4,240) # Height

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange (hsv, lower_blue, upper_blue)
    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
#        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)

#        print ('top_left_x = ' , xg)
#        print ('top_left_y = ' , yg)
#        print ('width = ' , wg)
#        print ('height = ' , hg)

        xc = xg + (wg / 2)
        yc = yg + (hg / 2)

        px = int(68 + (0.1 * xc))
        py = int(80 - (0.2 * yc))

        if px > 67 and px < 101 and py > 29 and py < 81:
           cmd = "ola_streaming_client -u 1 -d {0},,{1}".format(px,py)
           os.system(cmd)

#       print("Center X: %s Y: %s" % (int(xc), int(yc)))

#       print("Palla X: %s Y: %s" % px, py)

#       cv2.circle(frame,(int(xc),int(yc)),2,(0,255,0),2)

#       cv2.imshow('frame',frame)

#    cv2.imshow('mask',mask)

    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()