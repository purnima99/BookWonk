import cv2
import os
import time
import shutil

from PIL import Image

path = "" #add path
im_list = []

os.mkdir(path)

os.chdir(path)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    else:
        # SPACE pressed
        time.sleep(2)
        img_name = "img{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        one = os.path.join("", img_name) #add path
        im = Image.open(one)
        im_list.append(im)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# im_list = [im1,im2,im3]

pdf1_filename = "" #add path

im.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)

#shutil.rmtree(path)
