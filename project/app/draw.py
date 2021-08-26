import cv2
import numpy as np


drawing = False
mode = False
ix = -1
iy = -1
def ve_so(event, x, y, flags, param):
	global mode
	if event == cv2.EVENT_LBUTTONDBLCLK:
		mode = True
		cv2.circle(img, (x,y), 5, (0,0,255), -1)
	elif event == cv2.EVENT_MOUSEMOVE:
		if mode == True:
			cv2.circle(img, (x,y), 5, (0,0,255), -1)
	elif event == cv2.EVENT_RBUTTONDBLCLK:
		mode = False

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", ve_so)

while 1:
	cv2.imshow("image", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
