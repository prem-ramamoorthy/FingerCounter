import cv2 as cv
import handDetection as hd 
import time as t 
import os

wcam , hcam = 640 , 480 

vid = cv.VideoCapture(0)
vid.set(3,wcam)
vid.set(4,hcam)
ptime = 0
detector = hd.handDetection(detectionCon=0.7)
imagesPath = r"FingerCounter\images"
overlays = []

for imgpath in os.listdir(imagesPath) :
    image = cv.imread(f"{imagesPath}/{imgpath}")
    overlays.append(image)
    
tipIDs = [4,8,12,16,20]    
h,w,_ = overlays[0].shape
    
while True :
    isTrue , frame = vid.read()
    if not isTrue :
        break
    
    frame = detector.findHands(frame) 
    lmlist = detector.findposition(frame , draw= False)
    if len(lmlist) != 0 :
        openfingers = []
        
        if lmlist[tipIDs[0]][1] > lmlist[tipIDs[0] - 1][1]:
            openfingers.append(1)
        else:
            openfingers.append(0)
            
        for id in range(1, len(tipIDs)):
            if lmlist[tipIDs[id]][2] < lmlist[tipIDs[id] - 2][2]:
                openfingers.append(1)
            else:
                openfingers.append(0)

        totalfingerOpen = openfingers.count(1)
        frame[30:h+30 , 0:w ] = overlays[totalfingerOpen]
        
        cv.putText(frame , str(totalfingerOpen) ,(30 , w+90) , cv.FONT_HERSHEY_SIMPLEX , 3 , (255,0,255) , 10 )
        
    ctime = t.time()
    fps = 1/ (ctime - ptime)
    ptime = ctime
    
    cv.putText(frame , f"FPS : {int(fps)}"  , (10,25) , cv.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255) , 2)
    cv.imshow('Video' , frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
            break
        
vid.release()
cv.destroyAllWindows()