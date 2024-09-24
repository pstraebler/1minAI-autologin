from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time
import argparse

load_dotenv()
parser = argparse.ArgumentParser()

#liqte des arguments possibe
parser.add_argument('--headless', action='store_true', help='Exécute le script en mode headless')

#analyse des arguments
args = parser.parse_args()

chrome_options = Options()

if args.headless:
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

#browser=webdriver.Chrome()
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://app.1min.ai/")

time.sleep(2)

#fermer la popup de presentation
browser.find_element(By.CLASS_NAME, "ant-tour-close").click()
time.sleep(1)

#click on login (thanks gpt-01)
browser.find_element(By.XPATH, '//button[contains(@class, "ant-btn") and contains(@class, "ant-btn-primary")]/span[text()="Log In"]/..').click()

time.sleep(1)

#fill username / password
browser.find_element(By.ID, "login_email").send_keys(os.getenv("USERNAME"))
browser.find_element(By.ID, "login_password").send_keys(os.getenv("PASSWORD"))
time.sleep(1)

#login
browser.find_element(By.CSS_SELECTOR, "button.ant-btn.css-nqmzah.ant-btn-primary[type='submit']").click()

time.sleep(5)

browser.close()
