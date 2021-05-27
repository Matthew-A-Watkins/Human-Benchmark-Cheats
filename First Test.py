import webbrowser
from time import sleep
import pyautogui

def main():
    # green_hex = '4bdb6a'
    # red_hex = 'ce2636'
    # blue_hex = '2b87d1'

    # init iterations
    # open web page
    webbrowser.open("https://humanbenchmark.com/tests/reactiontime", new=2)
    sleep(3)
    img = pyautogui.screenshot()

    # find size of monitor
    current_pixel = pyautogui.position()

    # get current color 
    print(current_pixel)
    current_rgb = img.getpixel(current_pixel)
    currentHexColor = '%02x%02x%02x' % current_rgb

    if currentHexColor == '2b87d1':
        pyautogui.click()
        for i in range(5):
            # waits until the current color is green
            while currentHexColor != '4bdb6a':
                img = pyautogui.screenshot()
                current_rgb = img.getpixel(current_pixel)
                currentHexColor = '%02x%02x%02x' % current_rgb

            pyautogui.click()
            sleep(0.16)
            pyautogui.click()

            currentHexColor = ''

if __name__ == '__main__':
    main()