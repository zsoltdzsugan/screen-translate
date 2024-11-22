# app/app_class.py
from app.gui import Gui
from app.screenshot_class import ScreenshotClass
from services.text_extractor import TextExtractor

class Application:
    def __init__(self):
        self.screenshotter = ScreenshotClass()
        self.text_extractor = TextExtractor()
        self.translation_language = "Hungarian"
        self.gui = Gui(self)

    def take_screenshot(self):
        return self.screenshotter.save_screenshot()

    def extract_text(self, image_path):
        return self.text_extractor.extract_text(image_path)

    def run(self):
        print("App started")
        self.gui.run()

