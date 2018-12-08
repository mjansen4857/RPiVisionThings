from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
camera.framerate = 30
camera.shutter_speed = 33333
#camera.awb_mode = 'auto'
camera.exposure_mode = 'off' #off

rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

hsv = np.zeros((640, 480, 3), np.uint8)
hsv_low = [50, 60, 100]
hsv_high = [80, 255, 255]

cv2.namedWindow('Vision')

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv_thresh = cv2.inRange(hsv, np.array(hsv_low), np.array(hsv_high))
    
    im2, contours, hierarchy = cv2.findContours(hsv_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.drawContours(image, [cv2.convexHull(contour)], -1, (0,0,255), 1)
    
    # show the frame
    cv2.imshow('Vision', image)
    cv2.imshow('thresh', hsv_thresh)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

