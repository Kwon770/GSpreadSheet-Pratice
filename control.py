from pyautogui import mouseDown, hotkey, press, click, FAILSAFE
from time import sleep

FAILSAFE = False


def StartPrintControl():
    # left window pos
    mouseDown(x=630, y=40, button='left')
    click(x=630, y=40, button='left')
    hotkey('command', 'p')
    sleep(0.5)
    press('tab')
    press('enter')
    sleep(3)
    hotkey('command', 'p')
    sleep(0.5)
    press('enter')
    sleep(2)
    hotkey('command', 'w')


def MoveFirstSheet():
    mouseDown(x=630, y=40, button='left')
    click(x=630, y=40, button='left')
    sleep(0.5)
    hotkey('option', 'up')


def MoveFocusToTerminal():
    # right window pos
    mouseDown(x=1100, y=35, button='left')
    click(x=1100, y=35, button='left')
