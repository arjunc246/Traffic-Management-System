# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:41:17 2019

@author: DELL
"""

import cv2
import numpy as np
#import xlsxwriter

#workbook = xlsxwriter.Workbook('differenceFinal.xlsx')
#worksheet = workbook.add_worksheet()
#Trackbars



kernel = np.ones((15,15),np.uint8)

if __name__=="__main__":
    top, right, bottom, left = 5, 10, 280, 180
    vid=cv2.VideoCapture('latestData.mp4')
    refIm=cv2.imread('refFrame.jpg')
    refIm2=cv2.cvtColor(refIm, cv2.COLOR_BGR2GRAY)
    #rint(refIm)
   
    #vid.set(1, 3250)
    #ret, frame = vid.read()
    #cv2.imwrite('C:/Users/DELL/Google Drive (17dcs011@charusat.edu.in)/InternshalaHackathon/Video Dataset/refFrame.jpg', frame)
    vid.set(1,5000)
    #fgbg = cv2.createBackgroundSubtractorMOG2()
    #print(type(refIm))
    while(vid.isOpened()):
        ret,frame=vid.read()
        (h, w) = frame.shape[:2]
        #print(h,w)
        vidClone=frame.copy()
        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            y=type(gray)
            #print(y)
            bg=refIm2.copy().astype('float')
            diff = cv2.absdiff(bg.astype('uint8'), gray)
            
            #xorRes = cv2.bitwise_xor(bg.astype(y),gray)
            #row=0
            #for col, data in enumerate(diff):
             #   worksheet.write_column(row, col, data)
            #print(diff)
            thresholded = cv2.threshold(diff,70, 255, cv2.THRESH_BINARY)[1]
            #dilation = cv2.dilate(thresholded,kernel,iterations = 1)
            #cv2.imshow('dilation', dilation)
            erosion = cv2.erode(thresholded,kernel,iterations = 1)
            cv2.imshow('Check this', erosion)
            #cv2.imwrite('C:/Users/Deep Kaneria/Downloads/3.MorphologicalFilters/erosion_j.png0', erosion)

            cv2.imshow('Input',gray)
            cv2.imshow('Original',frame)
            cv2.imshow('Dif',thresholded)
            
            closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
            #cv2.imshow('closing', closing)
            opening = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
            cv2.imshow('opening', opening)
            
            keypress = cv2.waitKey(30) & 0xFF
            
            # if the user pressed "q", then stop looping
            if keypress == ord('q'):
                break
#workbook.close()
vid.release
cv2.destroyAllWindows()
        
    