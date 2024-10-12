from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import getpass
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

url = 'https://www.reddit.com/login/ '

driver.get(url)

time.sleep(3)

#Nhap thong tin ng dung
my_email = input("Please enter your username: ")
my_password = getpass.getpass("Please enter your password: ")

#Dang Nhap
#username_input = driver.find_element(By.XPATH, "//input@[id='login-username']")
#password_input = driver.find_element(By.XPATH, "//input@[id='login-password']")

#Nhan thong tin va nhan nut Enter
#username_input.send_keys(my_username)
#password_input.send_keys(my_password + Keys.ENTER)

actionChains = ActionChains(driver)
time.sleep(1)

for i in range(5):
    actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys(my_email).perform()
time.sleep(0.5)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()
#Sau khi dang nhap de trang load 5s
time.sleep(3)


#Truy cap Creat Post
url2 = 'https://www.reddit.com/user/NguyenHoangPhat/submit?type=TEXT'

driver.get(url2)
time.sleep(2)

for i in range(18):
    actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys('Test possttttt').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys('Hoang Phat Ho Nguyen').perform()

for i in range(2):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(10)
actionChains.send_keys(Keys.ENTER).perform()

