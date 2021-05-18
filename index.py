import numpy as np
import cv2
from mss import mss
from PIL import Image

green_a = cv2.imread('assets/green_a.png', 0)
red_a = cv2.imread('assets/red_a.png', 0)
yellow_a = cv2.imread('assets/yellow_a.png', 0)
blue_a = cv2.imread('assets/blue_a.png', 0)
orange_a = cv2.imread('assets/orange_a.png', 0)

green = cv2.imread('assets/green.png', 0)
red = cv2.imread('assets/red.png', 0)
yellow = cv2.imread('assets/yellow.png', 0)
blue = cv2.imread('assets/blue.png', 0)
orange = cv2.imread('assets/orange.png', 0)
track = cv2.imread('assets/track.png', 0)

cords = {'top':420 , 'left': 360 , 'width': 820, 'height': 580 }

def matches(original, gray, template):
  w, h = template.shape[::-1]
  method = cv2.TM_SQDIFF_NORMED
  res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
  threshold = 0.9
  loc = np.where( res >= threshold)
  for pt in zip(*loc[::-1]):
    cv2.rectangle(original, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

while 1:
  with mss() as sct :
    img_rgb = np.array(sct.grab(cords))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('test', green)

    matches(img_rgb, img_gray, green)
    matches(img_rgb, img_gray, red)
    matches(img_rgb, img_gray, yellow)
    matches(img_rgb, img_gray, blue)
    matches(img_rgb, img_gray, orange)

    cv2.imshow('Detected',img_rgb)


    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break
    