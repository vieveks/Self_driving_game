import numpy as np
import cv2
import time 
import mss
import mss.tools

capture = mss.mss()

monitor = {"top": 0, "left": 0, "width": 100, "height": 100}
#img = np.array(capture.grab(monitor))

prev_time = 0

if __name__ == '__main__':
    
    while True:
        output = capture.grab(monitor)
        mss.tools.to_png(output.rgb, output.size, output="images/screenshot.png")
        time_per_loop = time.time() - prev_time
        prev_time = time.time()
        #print(time_per_loop)
        print(f'the fps = {1/time_per_loop}')
        #img = cv2.imread(np.array(png))
        #cv2.imshow('ImageWindow', png)
        #print(type(png))
        #cv2.imshow('image', output)
        #print(img.shape)

