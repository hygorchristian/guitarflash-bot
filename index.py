import pyautogui
import fpstimer

#assets
green = 'assets/green.png'
red = 'assets/red.png'
yellow = 'assets/yellow.png'
blue = 'assets/blue.png'
orange = 'assets/orange.png'
track = 'assets/track1.png'

FPS=60
timer = fpstimer.FPSTimer(FPS)
region=(278 * 2,703 * 2,922,166)

def loop():
  while (1):
    run()
    timer.sleep()

def run():
  tracklocation = pyautogui.locateOnScreen(yellow, region=region, confidence=0.7)
  print(tracklocation)

loop()