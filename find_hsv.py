import cv2
import numpy as np 

im = cv2.imread("green.png", cv2.IMREAD_UNCHANGED)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

cv2.imshow("original", im)
cv2.imshow("hsv", hsv)

means = np.mean(hsv, 2)
print(hsv)
print(hsv.shape)
print(len(hsv.shape))
				 #for dirt
h = hsv[:, : ,0] #average is 17.9
s = hsv[:, :, 1] #average is 22.21
v = hsv[:, :, 2] #average is 156.12
#for "green"
#h = 45
#s = 71
#v = 132


cv2.waitKey(0)
cv2.destroyAllWindows()