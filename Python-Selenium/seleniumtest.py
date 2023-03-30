#!/bin/zsh
# Source: https://chromedriver.chromium.org/getting-started

# --- test 1 (Works)

# import time

# from selenium import webdriver

# from selenium.webdriver.chrome.options import Options

# options = Options()

# options.binary_location = "/usr/share/applications/google-chrome.google-chrome.desktop"

# driver = webdriver.Chrome() # '/usr/bin/chromedriver' # Optional argument, if not specified will search path.

# driver.get('http://www.google.com/');

# time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# driver.quit()

# --- test 2 (For functions that involve datetime in meetcli and meetgui) (It works)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import datetime
from datetime import datetime
import pyautogui
from crdntl import mail_address, passgoog

# Selenium Driver variables

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
brave_path = "/usr/share/applications/google-chrome.desktop"

opt = Options()
opt.binary_location = brave_path # ESSENTIAL
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
# opt.add_argument('--start-maximized')
# opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
# opt.add_experimental_option('excludeSwitches', ['enable-logging'])
# opt.add_argument('--disable-blink-features=AutomationControlled')
# opt.add_experimental_option("prefs", {
  
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.geolocation": 0,
#     "profile.default_content_setting_values.notifications": 1
# })

driver = webdriver.Chrome() # service=service, 

# Datetime Variables

hour_now_format = datetime.now().isoformat(timespec='hours')   
hour_now = str(hour_now_format[11:13])

min_now_format = datetime.now().isoformat(timespec='minutes')   
min_now = str(min_now_format[14:16])

# Google Meet Functions

def Glogin(mail, pswrd):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.implicitly_wait(10)
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
  
    # input Password
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passgoog)
    driver.find_element_by_id("passwordNext").click()
  
    # go to google home page to keep login Wheen redirected to Meet.
    driver.get('https://google.com/')
    # pyautogui.press("F11")

def closing():

    closeprompt = pyautogui.confirm(text="Click Ok to end session.", title="End session?", buttons=['OK', 'Cancel'])

    if closeprompt == "OK":
        close = driver.close()
        close
        pyautogui.alert(text="Bye! Have a nice day!", title="Session ended.")
    elif closeprompt == "Cancel":
        return closeprompt
    else:
        pass

def any_sub():
    if datetime.today().weekday() == 6: # Change to current Time, 6 is sunday, 0 is monday, figure out the rest. 
        print("any_sub function passed.")
        if hour_now == "10": # Change to current Time, from the "input" to 1 hour after in millitary time.
            Glogin(mail_address, passgoog) # Returns security block after email part
            # driver.get("https://coalemus.github.io/Portfolio-Website")
            driver.implicitly_wait(10)
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

any_sub()