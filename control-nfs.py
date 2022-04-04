import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import pyautogui
import time
 
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
 
keyboard = Controller()
key1 = "w"
key2 = 'd'
key3 = 'a'


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw
 
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
 
        # print(len(lmList1),lmList1)
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        
 
 
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right
 
            fingers2 = detector.fingersUp(hand2)
            if hands  :
                keyboard.press(key1)
                time.sleep(0.01)
            else :
                keyboard.release(key1)
            if fingers2 == [1,1,1,1,1] :
                keyboard.press(key2)
                time.sleep(0.01)
            else :
                keyboard.release(key2)
            if fingers1 == [1,1,1,1,1] :
                keyboard.press(key3)
                time.sleep(0.01)
            else :
                keyboard.release(key3)  
                time.sleep(0.01)              
            
            #print(fingers1, fingers2)
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw
            #print(length)
        

    
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)


