import cv2
import time

vidcap = cv2.VideoCapture(r'H:\videos\output3dimensional.mp4')
# success,image = vidcap.read()
# print(success)
success = True
while success:
    t = time.time()
    t = int(round(t * 1000))
    success,image = vidcap.read()
    cv2.imwrite(r"H:\videos\output\frame%d.jpg" %t, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:
        break

