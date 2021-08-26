import eel
import cv2
import face_eye as FE
import sys
import numpy as np

eel.init("../app")
predict = 0

@eel.expose
def getFace_Eye():
	face_detection = cv2.CascadeClassifier("../data/haarcascade_frontalface_alt.xml")
	eye_detection  = cv2.CascadeClassifier("../data/haarcascade_eye_tree_eyeglasses.xml")
	cap = FE.Capture()
	try:
		return cap.setCamera(face_detection,eye_detection)
	except:
		print("error")
eel.start("2.html", size = (400,700))