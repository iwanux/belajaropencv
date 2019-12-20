import argparse
import cv2

# fetching argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading image dan dikonvert ke array numpy
image = cv2.imread(args["image"])


# ngambil value pixel di coordinat
(b,g,r) = image[0,0]
print("pixel di 0,0 red:{} green:{} blue:{}".format(r,g,b))

# setting pixel di coordinat
image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("pixel di 0,0 red:{} green:{} blue:{}".format(r,g,b))

corner = image[0:100,0:100]

image[100:200,100:200] = (0,255,0)

cv2.imshow('sudut',image)

# biar windownya kebuka
cv2.waitKey(0)