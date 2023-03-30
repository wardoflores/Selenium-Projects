#!/bin/zsh
# Adapted for Linux systems, Google login has a lock on Automated Browsers it seems.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import datetime
from datetime import datetime
import pyautogui
from crdntl import mail_address, passgoog

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Task Scheduler")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

titleframe = ttk.Frame(mainframe).grid(column=1, row=1, sticky=(N))
label = ttk.Label(titleframe, text='Task Scheduler: Paste the link to the current time.').grid(column=0, row=1, sticky=N)

ttk.Label(mainframe, text="Monday").grid(column=1, row=0, sticky=N)
ttk.Label(mainframe, text="Tuesday").grid(column=2, row=0, sticky=N)
ttk.Label(mainframe, text="Wednesday").grid(column=3, row=0, sticky=N)
ttk.Label(mainframe, text="Thursday").grid(column=4, row=0, sticky=N)
ttk.Label(mainframe, text="Friday").grid(column=5, row=0, sticky=N)
ttk.Label(mainframe, text="Anyday Test").grid(column=7, row=0, sticky=N)


ttk.Label(mainframe, text="1st Sub").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="2nd Sub").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="3rd Sub").grid(column=0, row=3, sticky=W)
ttk.Label(mainframe, text="4th Sub").grid(column=0, row=4, sticky=W)


# Change these Meeting links every week, check for new links.

# # Anytime Test
# anydaylink1 = StringVar()
# anydaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=anydaylink1)
# anydaylink1_entry.grid(column=7, row=1, sticky=(W, E))

# anydaylink1set = StringVar()

# anydaylink1set.set(anydaylink1)

# root.bind("<Return>", any_sub)

# Monday Subjects
mondaylink1 = StringVar()
mondaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=mondaylink1)
mondaylink1_entry.grid(column=1, row=1, sticky=(W, E))

mondaylink2 = StringVar()
mondaylink2_entry = ttk.Entry(mainframe, width=7, textvariable=mondaylink2)
mondaylink2_entry.grid(column=1, row=2, sticky=(W, E))

mondaylink3 = StringVar()
mondaylink3_entry = ttk.Entry(mainframe, width=7, textvariable=mondaylink3)
mondaylink3_entry.grid(column=1, row=3, sticky=(W, E))

mondaylink4 = StringVar()
mondaylink4_entry = ttk.Entry(mainframe, width=7, textvariable=mondaylink4)
mondaylink4_entry.grid(column=1, row=4, sticky=(W, E))


# Tuesday Subjects
tuesdaylink1 = StringVar()
tuesdaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=tuesdaylink1)
tuesdaylink1_entry.grid(column=2, row=1, sticky=(W, E))

tuesdaylink2 = StringVar()
tuesdaylink2_entry = ttk.Entry(mainframe, width=7, textvariable=tuesdaylink2)
tuesdaylink2_entry.grid(column=2, row=2, sticky=(W, E))

tuesdaylink3 = StringVar()
tuesdaylink3_entry = ttk.Entry(mainframe, width=7, textvariable=tuesdaylink3)
tuesdaylink3_entry.grid(column=2, row=3, sticky=(W, E))

tuesdaylink4 = StringVar()
tuesdaylink4_entry = ttk.Entry(mainframe, width=7, textvariable=tuesdaylink4)
tuesdaylink4_entry.grid(column=2, row=4, sticky=(W, E))

# Wednesday Subjects
wednesdaylink1 = StringVar()
wednesdaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=wednesdaylink1)
wednesdaylink1_entry.grid(column=3, row=1, sticky=(W, E))

wednesdaylink2 = StringVar()
wednesdaylink2_entry = ttk.Entry(mainframe, width=7, textvariable=wednesdaylink2)
wednesdaylink2_entry.grid(column=3, row=2, sticky=(W, E))

wednesdaylink3 = StringVar()
wednesdaylink3_entry = ttk.Entry(mainframe, width=7, textvariable=wednesdaylink3)
wednesdaylink3_entry.grid(column=3, row=3, sticky=(W, E))

wednesdaylink4 = StringVar()
wednesdaylink4_entry = ttk.Entry(mainframe, width=7, textvariable=wednesdaylink4)
wednesdaylink4_entry.grid(column=3, row=4, sticky=(W, E))

# Thursday Subjects
thursdaylink1 = StringVar()
thursdaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=thursdaylink1)
thursdaylink1_entry.grid(column=4, row=1, sticky=(W, E))

thursdaylink2 = StringVar()
thursdaylink2_entry = ttk.Entry(mainframe, width=7, textvariable=thursdaylink2)
thursdaylink2_entry.grid(column=4, row=2, sticky=(W, E))

thursdaylink3 = StringVar()
thursdaylink3_entry = ttk.Entry(mainframe, width=7, textvariable=thursdaylink3)
thursdaylink3_entry.grid(column=4, row=3, sticky=(W, E))

thursdaylink4 = StringVar()
thursdaylink4_entry = ttk.Entry(mainframe, width=7, textvariable=thursdaylink4)
thursdaylink4_entry.grid(column=4, row=4, sticky=(W, E))

# Friday Subjects
fridaylink1 = StringVar()
fridaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=fridaylink1)
fridaylink1_entry.grid(column=5, row=1, sticky=(W, E))

fridaylink2 = StringVar()
fridaylink2_entry = ttk.Entry(mainframe, width=7, textvariable=fridaylink2)
fridaylink2_entry.grid(column=5, row=2, sticky=(W, E))

fridaylink3 = StringVar()
fridaylink3_entry = ttk.Entry(mainframe, width=7, textvariable=fridaylink3)
fridaylink3_entry.grid(column=5, row=3, sticky=(W, E))

fridaylink4 = StringVar()
fridaylink4_entry = ttk.Entry(mainframe, width=7, textvariable=fridaylink4)
fridaylink4_entry.grid(column=5, row=4, sticky=(W, E))

# root.mainloop()

# Selenium Driver variables

driver_path = "/usr/bin/chromedriver"
browser_path = "/usr/share/applications/google-chrome.desktop"

opt = Options()
opt.binary_location = browser_path
# opt = webdriver.ChromeOptions()
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

#driver = webdriver.Chrome() # service=service, options=opt | Uncomment to start regardless of conditions.

# Datetime Variables
hour_now_format = datetime.now().isoformat(timespec='hours')   
hour_now = str(hour_now_format[11:13])

min_now_format = datetime.now().isoformat(timespec='minutes')   
min_now = str(min_now_format[14:16])

# Google Meet Functions
def Glogin(mail, pswrd):
    
    driver = webdriver.Chrome()
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
    pyautogui.press("F11")

# explicit function to turn off mic and cam
def turnOffMicCam():
  
    # turn off Microphone
    driver.implicitly_wait(10)
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('d') # press d key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath( 
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
  
    # turn off camera
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('e') # press e key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath(
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()

def AskToJoin():
    # Ask to Join meet
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

def joinNow():
    # Join meet
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

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

# meetinglink = pyautogui.prompt(title="Google meet automation", text="Input meeting link:")

# Datetime Scheduling of Code and dynamic Meeting link variable Execution.
#TODO: number out the subs and append the meetinglink entry form there.

def any_sub(anydaylink1set):
    # Glogin(mail_address, passgoog)
    driver = webdriver.Chrome()
    anydaylink1set = str(anydaylink1set)
    print(anydaylink1set)
    driver.get(anydaylink1set) # https://coalemus.github.io/Portfolio-Website/
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

# Anytime Test
anydaylink1 = StringVar()
anydaylink1_entry = ttk.Entry(mainframe, width=7, textvariable=anydaylink1)
anydaylink1_entry.grid(column=7, row=1, sticky=(W, E))

anydaylink1set = StringVar()

anydaylink1set.set(str(anydaylink1.get))

root.bind("<Return>", any_sub) # any_sub

root.mainloop()

def mon_sub1():
    Glogin(mail_address, passgoog)
    driver.get(mondaylink1)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def mon_sub2():
    Glogin(mail_address, passgoog)
    driver.get(mondaylink2)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def mon_sub3():
    Glogin(mail_address, passgoog)
    driver.get(mondaylink3)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def mon_sub4():
    Glogin(mail_address, passgoog)
    driver.get(mondaylink4)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def tue_sub1():
    Glogin(mail_address, passgoog)
    driver.get(tuesdaylink1)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def tue_sub1():
    Glogin(mail_address, passgoog)
    driver.get(tuesdaylink2)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def tue_sub3():
    Glogin(mail_address, passgoog)
    driver.get(tuesdaylink3)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def tue_sub4():
    Glogin(mail_address, passgoog)
    driver.get(tuesdaylink4)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def wed_sub1():
    Glogin(mail_address, passgoog)
    driver.get(wednesdaylink1)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def wed_sub2():
    Glogin(mail_address, passgoog)
    driver.get(wednesdaylink2)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def wed_sub3():
    Glogin(mail_address, passgoog)
    driver.get(wednesdaylink3)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def wed_sub4():
    Glogin(mail_address, passgoog)
    driver.get(wednesdaylink4)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def thur_sub1():
    Glogin(mail_address, passgoog)
    driver.get(thursdaylink1)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def thur_sub2():
    Glogin(mail_address, passgoog)
    driver.get(thursdaylink2)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def thur_sub3():
    Glogin(mail_address, passgoog)
    driver.get(thursdaylink3)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def thur_sub4():
    Glogin(mail_address, passgoog)
    driver.get(thursdaylink4)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def fri_sub1():
    Glogin(mail_address, passgoog)
    driver.get(fridaylink1)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def fri_sub2():
    Glogin(mail_address, passgoog)
    driver.get(fridaylink2)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def fri_sub3():
    Glogin(mail_address, passgoog)
    driver.get(fridaylink3)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def fri_sub4():
    Glogin(mail_address, passgoog)
    driver.get(fridaylink4)
    turnOffMicCam()
    AskToJoin()
    # joinNow()
    closing()

def time_scan():
    
    # Time checking function
    # if datetime.today().weekday() == 6: # Change to current Time, 6 is sunday, 0 is monday, figure out the rest.
    #     print("Guess for current wekday passed the Test.")
    #     if hour_now == "10": # Change to current Time, from the "input" to 1 hour after in millitary time.
    #         print("Guess for current hour of the weekday passed the Test.")

    if datetime.today().weekday() == 6:
        if hour_now == "13": 
            any_sub()

    if datetime.today().weekday() == 0: # Monday
        if hour_now == "08" or hour_now == "09": # 8am to 10am
            mon_sub1()
        if hour_now == "10" or hour_now == "11": # 10am - 12:00pm
            mon_sub2()
        if hour_now == "13" or hour_now == "14" and min_now <= "29": # 1:30pm - 2:30pm
            mon_sub3()
        if hour_now == "14" and min_now >= "30" or hour_now == "15" or hour_now == "16" and min_now <= "30": # 2:30pm - 4:30pm
            mon_sub4()

    if datetime.today().weekday() == 1: # Tuesday
        if hour_now == "08" or hour_now == "09": # 8am to 10am
            tue_sub1()
        if hour_now == "10" or hour_now == "11": # 10am - 12:00pm
            tue_sub2()
        if hour_now == "13" or hour_now == "14" and min_now <= "29": # 1:30pm - 2:30pm
            tue_sub3()
        if hour_now == "14" and min_now >= "30" or hour_now == "15" or hour_now == "16" and min_now <= "30": # 2:30pm - 4:30pm
            tue_sub4()

    if datetime.today().weekday() == 2: # Wednesday
        if hour_now == "08" or hour_now == "12": # 12:30pm: # 8am - 9am
            wed_sub1()

    if datetime.today().weekday() == 3: # Thursday
        if hour_now == "14" or hour_now == "15" or hour_now == "16": # 2:30pm to 4:30pm
            thur_sub1()

    if datetime.today().weekday() == 4: # Friday
        if hour_now == "08" or hour_now == "09": # 8am to 10pm
            fri_sub1()

# Test for Functionality, Comment out function for proper usage of Program.
# any_sub()

time_scan()