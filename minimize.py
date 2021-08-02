import win32gui, win32con

activeWindows = []

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        # print(hex(hwnd), win32gui.GetWindowText(hwnd))
        activeWindows.append(hwnd)

win32gui.EnumWindows(winEnumHandler, None)
# minimize = win32gui.GetForegroundWindow()

for i in activeWindows:
    win32gui.ShowWindow(i, win32con.SW_MINIMIZE)

# win32gui.ShowWindow(minimize, win32con.SW_MINIMIZE)
