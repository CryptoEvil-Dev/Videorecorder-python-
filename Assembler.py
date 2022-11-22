import cv2
import numpy as np
import glob

frameSize = (1920, 1080)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, frameSize)


for filename in glob.glob('Sequence/*'):
    img = cv2.imread(filename)
    out.write(img)


out.release()