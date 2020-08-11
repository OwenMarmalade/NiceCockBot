import time
import pyautogui

def sendScript():
    time.sleep(5)
    for i in range(1, 69):
        pyautogui.typewrite("Put Text Here", interval= 0)
        pyautogui.press('enter')

sendScript()
