import cv2
import sys
from datetime import datetime

# Định nghĩa màu và font chữ
font_scale = 1.1
thicknessRect = 5
thicknessText = 2
font = cv2.FONT_HERSHEY_SIMPLEX
colorText = (250, 0, 246)


# Khởi tạo bộ nhận dạng ảnh

# Lớp Thời Gian
class RealTime(object):
	def __init__(self):
		self.now = datetime.now()
	def getTime(self):
		time = self.now.strftime("%d/%m/%Y-%H:%M:%S")
		return time

# Các khối bao đối tượng
class DrawDetection(object):
	def getBox1(self,x,y):
		try:
			z = x+y
			return (x,y)
		except:
			return (0,0)
	def getBox2(self,x,y,w,h):
		return (x+w,y+h)

# Lớp nhận dạng khuôn mặt
class Detection(object):
	name1 = "face"
	name2 = "eyeLeft"
	name3 = "eyeRight"
	facecount = 0
	eyecount  = 0
	colorFace = (0,255,0)
	colorEye  = (255,0,0)

	# Hàm khởi tạo có tham số đầu vào
	def __init__(self, detection, gray):
		self.detection = detection
		self.gray = gray

	# Trả về ma trận 4xn ---> n ở đây là số người 
	def get(self):
		try:
			detect = self.detection.detectMultiScale(self.gray,1.3,5)
			return detect
		except:
			return None

# Lớp Camera
class Capture():
	def setCamera(self, face_detection, eye_detection):
		# Khởi tạo Camera
		
		cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		# Kiểm tra camera có mở hay không
		if cap.isOpened() == None:
			sys.exit("Cap is not open!")
		K = ""

		# Nhận dạng với video
		while True:
			ret, frame = cap.read()
			
			# Kiểm tra ret có hoạt động không
			if not ret:
				print("Cannot Connection!")
				break

			# Kết nối thành công
			frame = cv2.resize(frame, (1000,700))
			gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			gray  = cv2.equalizeHist(gray)
			Face  = Detection(face_detection, gray)
			Eyecount = 0
			
			# Vẽ hình nhận dạng
			for (x,y,w,h) in Face.get():
				# Vẽ mặt
				
				cv2.rectangle(frame, (x,y), (x+w,y+h), Face.colorFace, thicknessRect)
				cv2.putText(frame,Face.name1,(x-10,y-10),
					        font, font_scale, colorText, thicknessText, cv2.LINE_AA)
				Face.facecount += 1
				# Vẽ mắt
				faceRoi  = gray[y:y+h, x:x+w]
				colorRoi = frame[y:y+h, x:x+w]
				Eye = Detection(eye_detection, faceRoi)

				for (xe,ye,we,he) in Eye.get():
					
					if (xe > w/2 and ye <= h/2+y):
						cv2.rectangle(colorRoi, (xe,ye), (xe+we,ye+he), 
							          Eye.colorEye, thicknessRect)

						cv2.putText(colorRoi, Eye.name2, (xe-5,ye-5),
							        font, font_scale, colorText, 
							        thicknessText, cv2.LINE_AA)
						Eye.eyecount += 1

					elif (xe <= w/2 and ye <= h/2+y):
						cv2.rectangle(colorRoi, (xe,ye), (xe+we,ye+he), 
							          Eye.colorEye, thicknessRect)

						cv2.putText(colorRoi, Eye.name3, (xe-5,ye-5),
					                font, font_scale, colorText, 
					                thicknessText, cv2.LINE_AA)
						Eye.eyecount += 1
					Eyecount = Eye.eyecount
			
			# Đếm số khuôn mặt và số con mắt trong frame
			cv2.putText(frame, "Face:" + str(Face.facecount), (50,50), font, font_scale,
					    colorText, thicknessText, cv2.LINE_AA)

			cv2.putText(frame, "Eye:" + str(Eyecount), (50,100), font, font_scale,
					    colorText, thicknessText, cv2.LINE_AA)

			# Thời gian thực
			realTime = RealTime()
			cv2.putText(frame, realTime.getTime(), (500,100), font, font_scale,
					    colorText, thicknessText, cv2.LINE_AA)

			# Cách Tắt Camera
			cv2.putText(frame, "Enter \'q\' --> Exit", (50,650), font, (font_scale-0.4), (255,170,145),
				        thicknessText, cv2.LINE_AA)
			# show camera
			cv2.imshow("Frame", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				cap.release()
				cv2.destroyAllWindows()
				return frame