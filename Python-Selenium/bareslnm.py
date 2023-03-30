#!/bin/zsh
# Adapted for Linux systems, still doesn't work for it though.

import time
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
browser = webdriver.Chrome()

browser.get("https://www.google.com")

time.sleep(2)

browser.close()