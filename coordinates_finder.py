# pip install pyautogui
import pyautogui
import time

last_pos = None

try:
    while True:
        pos = pyautogui.position()

        if pos != last_pos:
            print(f"X: {pos.x}, Y: {pos.y}")
            last_pos = pos

        time.sleep(0.01)
except KeyboardInterrupt:
    print("Stopped.")
