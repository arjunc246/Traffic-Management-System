import cv2
import numpy as np
kernel = np.ones((10,10),np.uint8)

if __name__=="__main__":
    top, right, bottom, left = 5, 10, 280, 180
    vid=cv2.VideoCapture('latestData.mp4')
    refIm=cv2.imread('refFrame.jpg',0)
    #rint(refIm)
    
    #vid.set(1, 3250)
    #ret, frame = vid.read()
    #cv2.imwrite('C:/Users/DELL/Google Drive (17dcs011@charusat.edu.in)/InternshalaHackathon/Video Dataset/refFrame.jpg', frame)
    #vid.set(1,3250)
    #fgbg = cv2.createBackgroundSubtractorMOG2()
    print(type(refIm))
    while(vid.isOpened()):
        ret,frame=vid.read()
        (h, w) = frame.shape[:2]
        #print(h,w)
        vidClone=frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret==True:
            
            bg=refIm.copy().astype('float')
            diff = cv2.absdiff(bg.astype('uint8'), gray)
            thresholded = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            cv2.imshow('Input',frame)
            #cv2.imshow('Dif',thresholded)
            closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
            #cv2.imshow('closing', closing)
            opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
            cv2.imshow('opening', opening)
            
            keypress = cv2.waitKey(30) & 0xFF
            
            # if the user pressed "q", then stop looping
            if keypress == ord('q'):
                break
vid.release
cv2.destroyAllWindows()
        
    
