import pyautogui as pg

print(pg.size())


def check_checkbox():
    for idx in range(10):
        try:
            loc=pg.locateCenterOnScreen(image="checkbox.png", region=(100, 200, 500, 500)) #left, top, width, height
            print(loc)
            pg.click(loc)
            pg.sleep(2)
        except pg.ImageNotFoundException:
            print("not found")
            break

if __name__ == '__main__':
    check_checkbox()
