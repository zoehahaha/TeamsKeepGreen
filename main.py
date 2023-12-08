import pyautogui
import time

pyautogui.FAILSAFE = FALSE

while True:
  time.sleep(10)

# this for loop is used to move the mouse
for i in range(0,100):
  pyautogui.move(0,i*10)
pyautogui.click(x=0,y=1000) # click the left bottom corner of the screen

for i in range(0,3):
  pyautogui.press("shift")
