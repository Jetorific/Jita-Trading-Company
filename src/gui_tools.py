import pyautogui
import time

def gui_autopilot() -> None:
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')

def alt_tab() -> None:
    pyautogui.hotkey('alt', 'tab')