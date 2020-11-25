import cv2
import numpy as np
import imutils
import math
import random as rng
rng.seed(12345)

DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}


#camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('vidbar1.mp4')



frame_counter = 0

digit = []

limitmem = 59

contours = {}
#array of edges of polygon
approx = []

def nothing(x):
	pass









def angle(pt1,pt2,pt0):
	dx1 = pt1[0][0] - pt0[0][0]
	dy1 = pt1[0][1] - pt0[0][1]
	dx2 = pt2[0][0] - pt0[0][0]
	dy2 = pt2[0][1] - pt0[0][1]
	return float((dx1*dx2 + dy1*dy2))/math.sqrt(float((dx1*dx1 + dy1*dy1))*(dx2*dx2 + dy2*dy2) + 1e-10)





cv2.namedWindow('marking')


cv2.createTrackbar('H Lower','marking',134,255,nothing)
cv2.createTrackbar('H Higher','marking',255,255,nothing)
cv2.createTrackbar('S Lower','marking',42,255,nothing)
cv2.createTrackbar('S Higher','marking',255,255,nothing)
cv2.createTrackbar('V Lower','marking',138,255,nothing)
cv2.createTrackbar('V Higher','marking',255,255,nothing)
X = cv2.createTrackbar('X','marking',50,500,nothing)
Y = cv2.createTrackbar('Y','marking' ,163,500,nothing)
dX = cv2.createTrackbar('delta X','marking',117,500,nothing)
dY = cv2.createTrackbar('delta Y','marking',200,500,nothing)


while(1):
	ret,img = camera.read()
	#img = cv2.flip(img,1)

	hImg,wImg,_ = img.shape

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hL = cv2.getTrackbarPos('H Lower','marking')
	hH = cv2.getTrackbarPos('H Higher','marking')
	sL = cv2.getTrackbarPos('S Lower','marking')
	sH = cv2.getTrackbarPos('S Higher','marking')
	vL = cv2.getTrackbarPos('V Lower','marking')
	vH = cv2.getTrackbarPos('V Higher','marking')

	LowerRegion = np.array([hL,sL,vL],np.uint8)
	upperRegion = np.array([hH,sH,vH],np.uint8)

	redObject = cv2.inRange(hsv,LowerRegion,upperRegion)

	kernal = np.ones((1,1),"uint8")

	red = cv2.morphologyEx(redObject,cv2.MORPH_OPEN,kernal)
	red = cv2.dilate(red,kernal,iterations=1)

	res1=cv2.bitwise_and(img, img, mask = red)


	cv2.imshow("gambar1",res1)


	##
	frame_counter += 1

	#If the last frame is reached, reset the capture and the frame_counter
	if frame_counter == camera.get(cv2.CAP_PROP_FRAME_COUNT):
		frame_counter = 0 #Or whatever as long as it is the same as next line
		camera.set(cv2.CAP_PROP_POS_FRAMES, 0)



	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		camera.release()
		cv2.destroyAllWindows()
		break
	

	####
	
	res2 = res1.copy()
	gray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
	thresh1 = cv2.threshold(gray,100,255,cv2.THRESH_TOZERO)[1]
	blur = cv2.blur(thresh1, (2, 2))
	
	
	

	X = cv2.getTrackbarPos('X','marking')
	Y = cv2.getTrackbarPos('Y','marking')
	dX = cv2.getTrackbarPos('delta X','marking')
	dY = cv2.getTrackbarPos('delta Y','marking')
	res3 = blur[X:dX, Y:dY]
	res4 = res3.copy()


	cnts = cv2.findContours(res3.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	digitCnts = []
	for c in cnts:
		(x, y, w, h) = cv2.boundingRect(c)
		if w >= 3 and h >= 3:
			digitCnts.append(c)
			cv2.rectangle(res3,(x,y),(x+w,y+h),(255,130,255),2)
			roi1 = res4[y:y+h,x:x+w]
			roi1 = cv2.resize(roi1,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
			(koorY,koorX) = roi1.shape #ngebuat kotak sakti berdasarkan koordinat angka
			param = 20
	
			print("Y = ",round(koorY/16),"X = ",round(koorX/2)) #coba koor
			#satu blm di buat
			
			if roi1[round(1.2*koorY/4),round(koorX/4)] > param: #atas kiri
				if roi1[round(2.8*koorY/4),round(koorX/4)] > param: #bawah kiri
					if roi1[round(1.2*koorY/4),round(2.8*koorX/4)] > param: #kanan atas
						if roi1[round(koorY/2),round(koorX/2)] > param: #tengah2 blm cek
							print(8)
						else:
							print(0)
					else:
						print(6)
				else:	
					if roi1[round(koorY/14),round(koorX/2)] > param: #tengah atas blmcek
						if roi1[round(koorY/16),round(14*koorX/16)] > param: # kanan atas blmcek
							print(9)
						else :
							print(5)
						
					else:
						print(4)

			else :
				if roi1[round(2.8*koorY/4),round(koorX/4)] > 20: #bawah kiri
					print(2)
				else:
					if roi1[round(koorY/2),round(koorX/2)] > 20: #tengah2 blm cek
						print(3)
					else:
						print(7)
				




	

	
	cv2.imshow("img1 ",res3)
	cv2.imshow("img2",roi1)
	
