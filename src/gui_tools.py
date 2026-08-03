import pyautogui
import time

def gui_autopilot():
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')

def alt_tab():
    pyautogui.hotkey('alt', 'tab')