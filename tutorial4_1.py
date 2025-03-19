import numpy as np
import cv2

# cap = cv2.VideoCapture('data\AMAZING.mp4')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int( cap.get(4))


    # image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    a =cv2.line(smaller_frame,(0,0),(width,height),(0,255,0),10)

    #Drawing rectangle in the video picture
    a =cv2.rectangle(a,(200,200),(width-100,height-100),(255,0,0),5)

    #Drawing Circle to the vido frame
    a = cv2.circle(a,(width//2,height//2),100,(0,0,255),10)

    #writing on the video
    a = cv2.putText(a, "Hello, World!",(200,300),2,2,(255,255,255),2,cv2.FONT_ITALIC)

    cv2.imshow('frame', a)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f'the height of the image {height}')
print(f'the width of the image {width}')
