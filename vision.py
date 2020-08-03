import cv2
import os

os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = '0'
video = cv2.VideoCapture(0)

a = 0
color = None
c = 0
rgb = 0
while True:
    a += 1
    check, frame = video.read()
    key = cv2.waitKey(1)
    if(key==ord('q')):
        break
    if(key==ord('f')):
        if(c):
            c = 0
        else:
            c = 1
    
    if(key==ord('b') or rgb==1):
        rgb = 1
        frame[:, :, 1] = 0
        frame[:, :, 2] = 0
    if(key==ord('g') or rgb==2):
        rgb = 2
        frame[:, :, 0] = 0
        frame[:, :, 2] = 0
    if(key==ord('r') or rgb==3):
        rgb = 3
        frame[:, :, 0] = 0
        frame[:, :, 1] = 0
    if(key==ord('z')):
        rgb = 0
        color = None

    if(key==ord('1')):
        color = cv2.COLOR_BGR2GRAY
    elif(key==ord('2')):
        color = cv2.COLOR_BGR2HSV

    frame = cv2.cvtColor(frame, color)
    if(c):
        cv2.imshow("Video", frame)
    else:    
        cv2.imshow("Video", cv2.flip(frame, 1))


cv2.destroyAllWindows()

video.release()