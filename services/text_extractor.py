import pytesseract
import sys
import os

# Adjust the path to Tesseract based on whether running as a script or bundled app
if getattr(sys, 'frozen', False):
    # Running as a packaged executable
    tesseract_path = os.path.join(sys._MEIPASS, 'tesseract.exe')
    tessdata_path = os.path.join(sys._MEIPASS, 'tessdata')
else:
    # Running as a script (for development)
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path
    tessdata_path = r'C:\Program Files\Tesseract-OCR\tessdata'  # Adjust path

# Set the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Set the TESSDATA_PREFIX environment variable to the tessdata directory
os.environ['TESSDATA_PREFIX'] = tessdata_path

class TextExtractor:
    @staticmethod
    def extract_text(image_path):
        """Extract text from the given image."""
        try:
            return pytesseract.image_to_string(image_path)
        except Exception as e:
            return f"Error extracting text: {e}"

