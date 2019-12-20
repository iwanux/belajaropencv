import numpy as np
import cv2

# declare canvas
canvas = np.zeros((500,500,3),dtype="uint8")

# declare warna
hijau = (0,255,0)
merah = (0,0,255)

# buat garis
# cv2.line(canvas,(100,100),(200,200),hijau,5)
# cv2.line(canvas,(0,0),(100,100),merah,5)

# cv2.imshow("canvas cuy",canvas)

# biar windownya kebuka
# cv2.waitKey(0)

# buat kotak cuy
# cv2.rectangle(canvas,(10,10),(200,200),hijau)
# cv2.imshow("canvas cuy",canvas)
# cv2.waitKey(0)

# buat lingkarang cuy
# cv2.circle(canvas,(100,100),100,merah)
# # circle(canvas,titiktengah,radius,warnagaris)
# cv2.imshow("canvas cuy",canvas)
# cv2.waitKey(0)

# buat lingkaran lingkar lingkar

# (centerX,centerY) = (canvas.shape[1]//2,canvas.shape[0]//2)

# for r in range(100,200,10):
#     cv2.circle(canvas,(centerX,centerY),r,merah)
# cv2.imshow('lingkaran berlipat',canvas)
# cv2.waitKey(0)

