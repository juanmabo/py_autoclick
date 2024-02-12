import pyautogui
import time

# Set the interval between clicks in seconds
interval_minutes = int(input("Insert minutes: "))
interval_seconds = interval_minutes * 60

try:
    while True:
        # Perform a left mouse click
        pyautogui.click(button='left')
        
        # Wait for the specified interval
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("Script stopped by user.")