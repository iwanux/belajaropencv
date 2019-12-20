import argparse
import cv2

# fetching argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading image dan dikonvert ke array numpy
image = cv2.imread(args["image"])
print("width of the image in pixels is: {}".format(image.shape[1]))
print("height of the image in pixels is: {}".format(image.shape[0]))
print("channels present the image is: {}".format(image.shape[2]))

# load image into cv2 window
# wait for key press
# write image into another format
cv2.imshow("Image Title", image)
cv2.waitKey(0)
cv2.imwrite("newcat.jpg", image)

# running command : python index.py --image ../1_fetching_load_save/cat.jpeg