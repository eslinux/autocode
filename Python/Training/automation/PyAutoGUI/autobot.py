import pyautogui as pg

print(pg.size())

try:
    loc=pg.locateCenterOnScreen(image="search.png", region=(100, 900, 200, 200)) #left, top, width, height
    print(loc)
    pg.click(loc)
except pg.ImageNotFoundException:
    print("not found")
