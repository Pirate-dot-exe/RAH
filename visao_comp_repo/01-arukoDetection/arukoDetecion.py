import cv2 as cv
from cv2 import aruco
import numpy as np

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_marker = aruco.DetectorParameters_create()
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #reconhece e printa o ID dos markers reconhecidos 
    marker_corners, markers_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters= param_marker
    )
    #print(markers_IDs)
    for ids, corners in zip(markers_IDs, marker_corners):
        cv.polylines(
            frame, [corners.astype( np.int32)] , True, (0, 255, 255), 4, cv.LINE_AA
        )
        print(ids, " " , corners)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
