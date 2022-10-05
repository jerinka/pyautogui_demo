import pyautogui
import os
import Xlib.display
from time import sleep

# pip3 install selenium==4.2.0

from selenium import webdriver
from pyvirtualdisplay.smartdisplay import SmartDisplay

# pour visible=1, installer xserver-xephyr
# sinon, xfvb prend le dessus
display = SmartDisplay(visible=0, size=(1800, 1600))
display.start()

browser = webdriver.Firefox()
browser.get('https://duckduckgo.com/')
browser.save_screenshot('nrst.png')
print (browser.title)

# search = browser.find_element_by_id('search_form_input_homepage')
# search.send_keys("auie")

# la souris se déplace dans le SmartDisplay
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

#x, y = pyautogui.locateCenterOnScreen('duckduck.png', confidence=0.9)
x, y = pyautogui.locateCenterOnScreen(image='d.png', confidence=0.5)

print(x,y)
pyautogui.moveTo(x, y)#, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

sleep(1)

browser.save_screenshot('auie.png')
browser.quit()

display.stop()
