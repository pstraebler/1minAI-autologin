from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
import time
import argparse

load_dotenv()
parser = argparse.ArgumentParser()

#liqte des arguments possibe
parser.add_argument('--debug', action='store_true', help='Debug mode')
parser.add_argument('--headless', action='store_true', help='Headless mode')
parser.add_argument('--chrome', action='store_true', help='Use Chrome webdriver')
parser.add_argument('--firefox', action='store_true', help='Use Firefox webdriver')

#analyse des arguments
args = parser.parse_args()

if args.debug:
    print('Script parameters : ')
    print(args)

#le driver par défaut est chrome
if args.chrome and args.firefox:
      print('You\'re weird. I\'m going to use Chrome.')
      browser='chrome'
elif args.chrome:
      browser='chrome'
elif args.firefox:
      browser='firefox'
else:
      browser='chrome'

if args.debug:
      print('Selected web browser : ' + browser)

match browser:
      case 'chrome':
            from selenium.webdriver.chrome.options import Options
            browserOptions = Options()
            if args.headless:
                  browserOptions.add_argument("--headless") 
                  browserOptions.add_argument("--no-sandbox")
                  browserOptions.add_argument("--disable-dev-shm-usage")
            driver=webdriver.Chrome(options=browserOptions)
      case 'firefox':
            from selenium.webdriver.firefox.options import Options
            browserOptions = Options()
            if args.headless:
                  browserOptions.add_argument("--headless")
            driver = webdriver.Firefox(options=browserOptions)
      case _:
            print('Unknown error')
            exit(1)  

if args.debug:
      print('Browser parameters : ')
      print(browserOptions.arguments)

driver.get("https://app.1min.ai/")

time.sleep(2)

#fermer la popup de presentation
driver.find_element(By.CLASS_NAME, "ant-tour-close").click()
time.sleep(1)

#click on login (thanks gpt-01)
driver.find_element(By.XPATH, '//button[contains(@class, "ant-btn") and contains(@class, "ant-btn-primary")]/span[text()="Log In"]/..').click()

time.sleep(1)

#fill username / password
driver.find_element(By.ID, "login_email").send_keys(os.getenv("USERNAME"))
driver.find_element(By.ID, "login_password").send_keys(os.getenv("PASSWORD"))
time.sleep(1)

#login
driver.find_element(By.CSS_SELECTOR, "button.ant-btn.css-nqmzah.ant-btn-primary[type='submit']").click()

time.sleep(5)

driver.close()
