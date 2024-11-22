import pytesseract

class TextExtractor:
    @staticmethod
    def extract_text(image_path):
        """Extract text from the given image."""
        try:
            return pytesseract.image_to_string(image_path)
        except Exception as e:
            return f"Error extracting text: {e}"

