import tkinter as tk
from services.screen_capture import ScreenCapture
from services.text_extractor import TextExtractor
from services.ai_translator import get_translation

class Gui:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.title("Fordito")

        # Label and Button for Area Selection
        self.label = tk.Label(self.root, text="Click 'Select Area' to capture part of the screen.")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select Area", command=self.start_selection)
        self.select_button.pack(pady=10)

        # Create a Text widget for displaying feedback (translated text with wrapping and scrolling)
        self.feedback_text = tk.Text(self.root, wrap=tk.WORD, height=10, width=50, font=("Helvetica", 14))
        self.feedback_text.pack(pady=10)

        # Add a scrollbar for the Text widget
        self.scrollbar = tk.Scrollbar(self.root, command=self.feedback_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link the Scrollbar to the Text widget
        self.feedback_text.config(yscrollcommand=self.scrollbar.set)

        # Make the Text widget read-only initially
        self.feedback_text.config(state=tk.DISABLED)

        # Initialize ScreenCapture
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

            # Enable the Text widget for editing
            self.feedback_text.config(state=tk.NORMAL)

            # Clear the Text widget before inserting new content
            self.feedback_text.delete(1.0, tk.END)

            # Insert the extracted text into the Text widget
            self.feedback_text.insert(tk.END, f"Forditando Szoveg:\n{extracted_text}\n\n")

            # Translate the extracted text
            translated_text = get_translation(extracted_text)

            # Insert the translated text into the Text widget
            self.feedback_text.insert(tk.END, f"Forditott szoveg:\n{translated_text}")

            # Disable the Text widget to make it read-only again
            self.feedback_text.config(state=tk.DISABLED)

            print(translated_text)

        except Exception as e:
            self.feedback_text.config(state=tk.NORMAL)
            self.feedback_text.delete(1.0, tk.END)  # Clear any previous text
            self.feedback_text.insert(tk.END, f"Error: {e}")
            self.feedback_text.config(state=tk.DISABLED)

    def run(self):
        """Start the GUI."""
        self.root.mainloop()
