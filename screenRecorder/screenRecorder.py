import sys
sys.path
sys.executable

#import pyscreeze
import pyautogui
import cv2
import numpy as np
#from PIL import Image

resolution = (1920, 1080)

# Video Codec Specification
codec = cv2.VideoWriter_fourcc(*"XVID")

# output file specification
filename = "myRecording.avi"

# frame per second
fps = 60

# create a VideoWriter object
output = cv2.VideoWriter(filename, codec, fps, resolution)

# create an empty window to display the live recording
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# control the size of the live display window
cv2.resizeWindow("Live", 480, 270)

# screen record loop
while True:
    # take screenshots with pyautogui
    img = pyautogui.screenshot()

    # convert the screenshot to a numpy array
    frame = np.array(img)

    # convert it from BGR(blue, green red) to RGB(red, green, blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write it to the output file
    output.write(frame)

    # dispay the recording screen
    cv2.imshow("LIVE", frame)

    # stop the recording when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break


# release the video writer
output.release

# destroy/close all windows
cv2.destroyAllWindows()
