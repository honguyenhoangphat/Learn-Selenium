from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/Selenium/project2/geckodriver.exe"

# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
url = 'https://gochek.vn/collections/all'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(1)

# Tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(3)

# for k in range(40):
#     try:
#         # Lấy tất cả các button trên trang
#         buttons = driver.find_elements(By.TAG_NAME, "button")
#
#         # Duyệt qua từng button
#         for button in buttons:
#             # Kiểm tra nếu nội dung của button chứa "Xem thêm" và "sản phẩm"
#             if "Xem thêm" in button.text and "sản phẩm" in button.text:
#                 # Di chuyển tới button và click
#                 button.click()
#                 break  # Thoát khỏi vòng lặp nếu đã click thành công
#
#     except Exception as e:
#         print(f"Lỗi: {e}")

# Nhấn phím mũi tên xuống nhiều lần để cuộn xuống từ từ
for i in range(40):  # Lặp 30 lần, mỗi lần cuộn xuống một ít
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)  # Tạm dừng 0.2 giây giữa mỗi lần cuộn để trang tải nội dung


# Tao cac list
stt = []
name = []
price = []
image = []

# Tìm tất cả các button có nội dung là "Chọn mua"
buttons = driver.find_elements(By.XPATH, "//button[text()='Chọn mua']")

# print(len(buttons))
#products = driver.find_elements(By.TAG_NAME, "col-md-3 col-sm-4 col-xs-6 pro-loop col_fix20")
# lay tung san pham
for product in enumerate(products):
    # Quay ngược 3 lần để tìm div cha
    # parent_div = bt
    # for _ in range(3):
    #     parent_div = parent_div.find_element(By.XPATH,"./..")  # Quay ngược 1 lần
    
    # sp =parent_div
    
    # Lay ten sp
    try:
        name = product.find_element(By.CLASS_NAME, 'h3').text
    except:
        name=''

    # Lay gia sp
    try:
        price = product.find_element(By.CLASS_NAME, 'pro-price_highlight').text
    except:
        price=''

    # Lay hinh anh
    try:
        image = product.find_element(By.TAG_NAME, 'product-img').get_attribute('src')
    except:
        image=''

    # Chi them vao ds neu co ten sp
    if(len(name)>0):
        stt.append(i)
        name.append(name)
        price.append(price)
        image.append(image)

# Tạo df
df=pd.DataFrame({
    "STT" : stt,
    "Tên sản phẩm": name,
    "Giá bán":price,
    "Hình ảnh":image

})

df.to_excel('sp_gocheck.xlsx', index=False)