from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

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
url = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?brand=25643'
#Truy cập
driver.get(url)

#Tạm dừng 3s
time.sleep(3)

body = driver.find_element(By.TAG_NAME, 'body')
for i in range(100):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.25)
time.sleep(5)

#Tao cac list
stt = []
ten_san_pham = []
gia_ban = []
hinh_anh = []

#Lay danh sach cac the div chua sp
sp_divs = driver.find_elements(By.CSS_SELECTOR, '.style__ProductLink-sc-139nb47-2.cKoUly.product-item')
print(len(sp_divs))

for i, sp in enumerate(sp_divs, 1):
    stt.append(i)

try:
    tsp = sp.find_element(By.TAG_NAME, 'h3').text
except:
    tsp = ''
    tsp.append(ten_san_pham)

try:
    gia = sp.find_element()
except:
    gia = ''
    gia.append(gia_ban)
driver.quit()