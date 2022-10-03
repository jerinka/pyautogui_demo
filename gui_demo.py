#!/usr/bin/env python3

import os

import pyautogui
import Xlib.display
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay
import cv2
import sys
python = sys.executable

window_width = 1200
window_height = 800

# PyVirtualDisplay
display = SmartDisplay(visible=False, size=(window_width, window_height))
display.start()

# PyAutoGUI
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

# Do your thing
pyautogui_window_width, pyautogui_window_height = pyautogui.size()
print("Screen size: {}x{}".format(pyautogui_window_width, pyautogui_window_height))

p = EasyProcess([python, 'script.py'])
p.start()
p.sleep(1)
x, y = pyautogui.locateCenterOnScreen(image='g.png', confidence=0.9)
print(x, y)

pyautogui.moveTo(x, y)
pyautogui.click()

p.stop()

display.stop()
print('>>> All done.')
