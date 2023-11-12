

import sys
import os
import glob
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time


def test_click_element():
    print("test_click_element")

    url = "https://selenium-python.readthedocs.io/getting-started.html"
    driver = webdriver.Chrome() 
    driver.get(url)

    # assert "Python" in driver.title
    elem = driver.find_element(By.XPATH, "//a[@href='navigating.html']")  #href="navigating.html"
    # elem.clear()
    # elem.send_keys("python")
    # elem.send_keys(Keys.RETURN)
    print(elem)
    if not elem is None:
        elem.click()

        # or below
        # ActionChains(driver)\
        #     .click(elem)\
        #     .perform()
    

    assert "No results found." not in driver.page_source
    time.sleep(20)
    driver.close()





def main():
    test_click_element()

    

if __name__ == '__main__':
    print("\n\n----- MAIN Start------")
    main()
    print("----- MAIN End------")