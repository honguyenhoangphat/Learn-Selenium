from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#Đường dẫn đến file geckodriver
gecko_path = "D:/Selenium/project2/geckodriver.exe"

#Khởi tạo tới đtuong dvu với đường geckodriver
ser = Service(gecko_path)

#Tạo tuỳ chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
#Thit lập firefox chỉ hiện thị giao diện
options.headless = False

#Khởi tạo driver
driver = webdriver.Firefox(service=ser, options=options)

#Tạo url
url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'
#Truy cập
driver.get(url)

#In ra nd trang web
print("Before: ===============\n")
print(driver.page_source)

#Tạm dừng 3s
time.sleep(3)

#In lại
print("\n\n\n\n After: ================\n")
print(driver.page_source)

driver.quit()