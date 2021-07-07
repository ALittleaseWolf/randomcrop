import os
import cv2
import time
import random

fps = 10
H,W = 480,640
filename = "girls"

date = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(int(round(time.time()*1000))/1000))
date = date.split("-")[:-1]
date = "".join(date)
save_name = date + ".mp4"
save_name = os.path.join("videos", save_name)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(save_name, fourcc, fps, (W,H))

filelist = os.listdir(filename)
random.shuffle(filelist)
elem = random.choice(filelist)
for im_file in filelist:
    im_path = os.path.join(filename,im_file)
    im = cv2.imread(im_path)
    im = cv2.resize(im,(W,H))
    video_writer.write(im)

for i in range(20): #2s
    im_path = os.path.join(filename,elem)
    im = cv2.imread(im_path)
    im = cv2.resize(im,(W,H))
    video_writer.write(im)

video_writer.release()

