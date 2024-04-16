

# https://www.w3schools.com/python/default.asp

import sys
import os
import glob
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook
from datetime import datetime

SCROLL_SLEEP=5 #second

def driver_sleep(duration = 1):
    time.sleep(duration)

def test_click_nextbtn():
    element_nextprev = driver.find_element(By.CLASS_NAME, "nextprev")
    element_btnnext = element_nextprev.find_element(By.CLASS_NAME, "w3-right")
    element_btnnext.click()

def test_search():
    element_search_inputtextbox = driver.find_element(By.ID, "tnb-google-search-input")
    element_search_button = driver.find_element(By.ID, "tnb-google-search-submit-btn")
    driver_sleep()
    element_search_inputtextbox.send_keys("javascript")
    driver_sleep()
    element_search_button.click()
    
if __name__ == '__main__':
    url = "https://www.w3schools.com/python/default.asp"
    print("open: ", url)

    driver = webdriver.Chrome() 
    driver.get(url)

    driver_sleep(10)










