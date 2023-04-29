import argparse 
from asyncio.windows_events import NULL
import time
import cv2
import sys
import imutils
from imutils.video import VideoStream

import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=str,
	default="DICT_5X5_250",
	help="type of ArUCo tag to detect")
args = vars(ap.parse_args())

ARUCO_DICT = {
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
}

if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		args["type"]))
	sys.exit(0)

print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters_create()

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

discoTracking = cv2.imread("source/Cap2.png")
print(discoTracking)
box = cv2.selectROI("Select disk area", discoTracking, fromCenter=False)
tracker = cv2.TrackerCSRT_create()
tracker.init(discoTracking, box)

while True:
	
	detectedListX = []	#===
	detectedListY = []
	frame = vs.read()
	frame = imutils.resize(frame, width=600)

	ok, box = tracker.update(frame)
	if ok:
		print(box)
		pt1 = (box[0], box[1])
		pt2 = ((box[0] + box[2]), (box[1] + box[3]))
		centerX = int ((box[0] + (box[0]+box[2]))/2)
		centerY = int ((box[1] + (box[1]+box[3]))/2)
		cv2.circle(frame, (centerX, centerY), 10, (0, 255, 0), 10)
		cv2.rectangle(frame, pt1, pt2, (255,0,0), 2, 1)
	else:
		print("Failed!")

	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
		arucoDict, parameters=arucoParams)
		
	if len(corners) > 0:
		# realiza um flatten da lista de Aruco ID's ??
		ids = ids.flatten()
		print(ids)

		for (markerCorner, markerID) in zip(corners, ids):

			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners

			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

			cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(frame, (cX, cY), 50, (5, 5, 255), -1)

			cv2.putText(frame, str(markerID),
				(topLeft[0], topLeft[1] - 15),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)
		
	cv2.imshow("Frame", frame)	#tela de saída
	key = cv2.waitKey(1) & 0xFF
	
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower = np.array([5, 5, 50])
	upper = np.array([60, 90, 255])
	mask = cv2.inRange(hsv_frame, lower, upper)
	cv2.imshow("HSV Image", mask)

	if key == ord("q"):	#quit
		break

cv2.destroyAllWindows()
vs.stop()