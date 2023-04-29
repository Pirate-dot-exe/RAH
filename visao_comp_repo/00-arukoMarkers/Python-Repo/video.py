import cv2

vs = VideoCapture(0)

while True:
    ret, frame = vs.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()
vs.stop()
