import pyautogui
import threading

print(pyautogui.size())
pyautogui.moveTo(500, 500) 
pyautogui.click()
pyautogui.click("fb.png")

count=0
for count in range(1,10):
    print(count)
    pyautogui.sleep(2)
    pyautogui.scroll(-100, 500, 500)
    pyautogui.click()
    pyautogui.write("hello")
    pyautogui.press("enter")
    

# pyautogui.click("fb.png")
