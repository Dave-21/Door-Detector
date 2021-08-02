import win32gui, win32con
import serial
import time

serCom = serial.Serial('COM5', 9600)
serCom.timeout = 1

activeWindows = []

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        activeWindows.append(hwnd)

while serCom.readable():
    if "open" in serCom.readline().decode():
        win32gui.EnumWindows(winEnumHandler, None)
        for i in activeWindows:
            win32gui.ShowWindow(i, win32con.SW_MINIMIZE)

        break