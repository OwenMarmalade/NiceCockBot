import time
import pyautogui

def sendScript():
    time.sleep(5)
    for i in range(1, 69):
        pyautogui.typewrite("Nice Cock", interval= 0)
        pyautogui.press('enter')

sendScript()