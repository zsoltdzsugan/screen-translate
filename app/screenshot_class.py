import pyautogui
import time

class ScreenshotClass:
    def __init__(self):
        pass

    def save_screenshot(self):
        filename = f"screenshot.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

        return filename
