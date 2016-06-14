import numpy as np
import cv2

#INPUT COLOR MIN AND MAX IN HSV
COLOR_MIN = np.array([10, 10, 100], np.uint8) #COLOR_MIN = np.array([0, 100, 0], np.uint8)
COLOR_MAX = np.array([20, 30, 200], np.uint8) #COLOR_MAX = np.array([255, 255, 255], np.uint8)


cap = cv2.VideoCapture('Video_Data/GOPR5503.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print("fps is "+str(fps))

dst = 0
non_colored = 0


while(cap.isOpened()):
	ret, frame = cap.read()
	height, width, channels = frame.shape
	num_pix = height*width
	if(not ret):
		print("Done!")
		break

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	dst = cv2.inRange(hsv, COLOR_MIN, COLOR_MAX)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask = dst)

	cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
	cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
	cv2.namedWindow('res', cv2.WINDOW_NORMAL)
		
	cv2.imshow('frame',frame)
	#cv2.resizeWindow('frame', 300, 300)
	cv2.imshow('dst',dst)
	#cv2.resizeWindow('dst', 300, 300)
	cv2.imshow('res',res)
	#cv2.resizeWindow('res', 300, 300)
		
	no_blue = cv2.countNonZero(dst)
	percent = 100*no_blue/ float(num_pix)
	print(str(percent))
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()