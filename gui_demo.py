#!/usr/bin/env python3

import os

import pyautogui
import Xlib.display
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

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

with EasyProcess(["xmessage", "hello"*30]) as proc:
    # wait until something is displayed on the virtual display (polling method)
    # and then take a fullscreen screenshot
    # and then crop it. Background is black.
    img = display.waitgrab()
    x, y = pyautogui.locateCenterOnScreen(image='ok1.png', confidence=0.9)

    print(x, y)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    proc.wait()


display.stop()
print('>>> All done.')
