import pyautogui

class ScreenCapture:
    def __init__(self):
        self.click_positions = []

    def record_click(self, x, y):
        """Record a click position."""
        self.click_positions.append((x, y))

    def reset_clicks(self):
        """Reset the recorded click positions."""
        self.click_positions = []

    def is_selection_complete(self):
        """Check if two clicks have been recorded."""
        return len(self.click_positions) == 2

    def get_selection_rectangle(self):
        """Get the rectangle coordinates from the two clicks."""
        if len(self.click_positions) != 2:
            raise ValueError("Selection is not complete.")
        (x1, y1), (x2, y2) = self.click_positions
        x_start, y_start = min(x1, x2), min(y1, y2)
        x_end, y_end = max(x1, x2), max(y1, y2)
        return x_start, y_start, x_end - x_start, y_end - y_start

    def take_screenshot(self, filename="screenshot.png"):
        """Take a screenshot of the selected area."""
        region = self.get_selection_rectangle()
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(filename)
        return filename

