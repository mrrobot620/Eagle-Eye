from selenium import webdriver
import os 
from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC3
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from idna import valid_contextj
from datetime import datetime, timedelta
from PIL import Image
from io import BytesIO


op = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,
    'download.default_directory' : r"C:\Users\abhishek.h1\Downloads\ee_data",
    'directory_upgrade': True
}
op.add_experimental_option('prefs' , prefs)
driver = webdriver.Chrome(options=op)
driver.get("https://eagleeye.portalonewifi.com/login")
time.sleep(5)
print(driver.title)

current_time = time.localtime()
current_datetime = datetime(*current_time[:6])
new_datetime = current_datetime - timedelta(minutes=5)

realtime = current_datetime.strftime("%H:%M")
date = new_datetime.strftime("%Y-%m-%d")
delayed_time = new_datetime.strftime("%H:%M")


print(date)
print(realtime)
print(delayed_time)
driver.maximize_window()


def login():
    username = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/input")
    username.send_keys("162575")
    password = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/input")
    password.send_keys("123456")
    sign_in = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/button")
    sign_in.click()
    return True


def date_time():
    from_date = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/input[2]")
    from_date.clear()
    time.sleep(1)
    from_date.send_keys("2023-10-01")
  










def search_shipment(tracking__id):
    search_field = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/input")
    search_field.send_keys(tracking__id)
    search_button = driver.find_element(By.XPATH  , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/button")
    search_button.click()
    time.sleep(0.1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    image = driver.get_screenshot_as_png()
    with open(f'{tracking__id.strip()}.png', 'wb') as f:
        f.write(image)
    search_field.clear()

    
login()
time.sleep(5)
date_time()
time.sleep(3)

with open('tid.txt' , 'r') as f:
    tids = f.readlines()

i = 0

for tid in tids:
    try:
        i += 1
        search_shipment(tid)
        print(f"Screenshot Saved:  {i}:  {tid}")
    except Exception as e:
        print(e)
