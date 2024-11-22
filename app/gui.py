import tkinter as tk
from services.screen_capture import ScreenCapture
from services.text_extractor import TextExtractor
from services.ai_translator import get_translation

class Gui:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.title("Fordito")

        self.label = tk.Label(self.root, text="Click 'Select Area' to capture part of the screen.")
        self.label.pack(pady=10)
        self.select_button = tk.Button(self.root, text="Select Area", command=self.start_selection)
        self.select_button.pack(pady=10)
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack(pady=10)

        self.capture = ScreenCapture()

    def start_selection(self):
        """Start the selection process."""
        self.capture.reset_clicks()
        self.overlay = tk.Toplevel(self.root)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-topmost", True)
        self.overlay.configure(bg="black")
        self.overlay.attributes("-alpha", 0.1)
        self.overlay.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        """Handle mouse clicks for area selection."""
        x, y = event.x_root, event.y_root
        self.capture.record_click(x, y)

        if self.capture.is_selection_complete():
            self.overlay.destroy()
            self.capture_area()

    def capture_area(self):
        """Capture the selected area and extract text."""
        try:
            screenshot_path = self.capture.take_screenshot()

            # Extract text from the screenshot
            extracted_text = TextExtractor.extract_text(screenshot_path)
            self.feedback_label.config(text=f"Extracted Text:\n{extracted_text}")

            # Translate the extracted text
            translated_text = get_translation(extracted_text)
            self.feedback_label.config(text=f"Translated Text:\n{translated_text}",font=("Helvetica", 14))

            print(translated_text)
        except Exception as e:
            self.feedback_label.config(text=f"Error: {e}")

    def run(self):
        """Start the GUI."""
        self.root.mainloop()
