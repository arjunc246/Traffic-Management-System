import cv2
import numpy as np

def fun(x):
    pass

canvas = np.ones((10, 10), np.uint8)

if __name__ == "__main__":
    #Parameters for croping#
    top, right, bottom, left = 5, 10, 280, 180


    vid = cv2.VideoCapture('latestData.mp4')
    refIm = cv2.imread('refFrame.jpg', 0)

    while (vid.isOpened()):
        ret, frame = vid.read()
        (h, w) = frame.shape[:2]
        vidClone = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret == True:
            bg = refIm.copy().astype('float')

            diff = cv2.absdiff(bg.astype('uint8'), gray)
            thresholded = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            #cv2.imshow('Input', frame)

            closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, canvas)
            #cv2.imshow('closing', closing)
            opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, canvas)
            #cv2.imshow('opening', opening)

            #k=cv2.getTrackbarPos("iteration","window")
            dilated=cv2.dilate(opening,None,iterations=17)
            _,contour,_=cv2.findContours(dilated ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
            #cv2.drawContours(vidClone,contour,-1,(0,255,0),3)
            #cv2.imshow("cloned",vidClone)
            for i in range(len(contour)):
                z=cv2.drawContours(vidClone,contour,i,(0,255,0))
                M=cv2.moments(contour[i])
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                area=cv2.contourArea(contour[i])
                cv2.putText(vidClone,str(area),(cx-10,cy-10),cv2.FONT_HERSHEY_SIMPLEX,0.3, (0, 0, 255), 2)

            cv2.imshow("cloned", vidClone)
            '''max=0
            for i in contour:
                print(cv2.contourArea(i))'''

            #cv2.imshow("dilated",dilated)
            keypress = cv2.waitKey(1) & 0xFF

            # if the user pressed "q", then stop looping
            if keypress == ord('q'):
                break

vid.release
cv2.destroyAllWindows()


