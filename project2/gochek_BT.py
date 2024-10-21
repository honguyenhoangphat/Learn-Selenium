from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/Selenium/project2/geckodriver.exe"

# Khởi tạo đối tượng dịch vụ với đường dẫn geckodriver
service = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=service)

# Tạo url
url = 'https://gochek.vn/collections/all'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(3)

# Tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(6)

# Nhấn phím mũi tên xuống nhiều lần để cuộn xuống từ từ
for i in range(20):  # Lặp 30 lần, mỗi lần cuộn xuống một ít
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)

# Tao cac list
product_name = []
price = []
price_original = []
image = []


products = driver.find_elements(By.XPATH, '//div[contains(@class,"product-block")]')
# lay tung san pham
for s, product in enumerate(products, 1):

    # Lay ten sp
    try:
        name = product.find_element(By.TAG_NAME, 'h3').text
    except:
        name=''

    # Lay gia sp
    try:
        sale = product.find_element(By.XPATH, './/p[contains(@class,"pro-price")]//span[1]').text
    except:
        sale=''

    # Lay gia gốc
    try:
        original = product.find_element(By.XPATH, './/p[contains(@class,"pro-price")]//del[1]').text
    except:
        original=''
    # Lay hinh anh
    try:
        img = product.find_element(By.TAG_NAME, "img").get_attribute('src')
    except:
        img=''

    # Chi them vao ds neu co ten sp
    if(len(name)>0):
       # stt.append(i)
        product_name.append(name)
        price.append(sale)
        price_original.append(original)
        image.append(img)

# Tạo df
df=pd.DataFrame({
    "Tên sản phẩm": product_name,
    "Giá bán":price,
    "Giá gốc":price_original,
    "Hình ảnh":image

})

df.to_excel('sp_gochek.xlsx', index=False)

driver.quit()