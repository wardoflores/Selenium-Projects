#!/bin/zsh

import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = "/home/joey/Drivers/chromedriver"
browser_path = "/usr/share/applications/google-chrome.desktop"

opt = Options()
opt.binary_location = browser_path
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
# opt.add_argument('--start-maximized')
# opt.add_experimental_option('excludeSwitches', ['enable-logging'])
# opt.add_argument('--disable-blink-features=AutomationControlled')

# Create new Instance of Brave
driver = webdriver.Chrome()

# driver.get("https://www. .com")
driver.get("https://www.gamesite.com")

time.sleep(1)

driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)

# pyautogui.keyDown('ctrl') # hold ctrl key
# pyautogui.press('e') # press e key
# pyautogui.keyUp('ctrl') # release ctrl key

time.sleep(1)

driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)

time.sleep(1)

driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)

time.sleep(1)

driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)

time.sleep(1)

driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)