import pyautogui, time
time.sleep(1)
pyautogui.press("win")
time.sleep(2)
pyautogui.write("notepad", interval = 0.2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Hello world!", interval = 0.2)


import pyautogui, time
time.sleep(2)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("youtube.com")
pyautogui.press("enter")
time.sleep(3)

# Click YouTube search bar (center-top area)
pyautogui.click(700, 150)
time.sleep(1)

pyautogui.write("programography", interval=0.1)
pyautogui.press("enter")

