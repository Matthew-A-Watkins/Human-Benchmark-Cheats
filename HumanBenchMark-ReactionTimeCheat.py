from ctypes import windll
import pyautogui
from time import sleep

# open ctypes library for graphics interface
gdi = windll.LoadLibrary("c:\\Windows\\system32\\gdi32.dll")

# green color used on benchmark
color = 7002955

# while True but 1 is directly considered True (for speed)
while 1:
    # current position of mouse.
    width, height = pyautogui.position()

    # use direct graphic interface in order to retrieve the pixel
    pixel = int(gdi.GetPixel(windll.user32.GetDC(0), width, height))

    # check for current color 
    if pixel == color:

        # click whe ncurrent color is given
        pyautogui.click()

        #short delay in order to not have overlap
        sleep(0.01)
