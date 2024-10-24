#Lấy ra tất cả các họa sĩ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Khoi tao WebDriver
drive = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/Lists_of_musicians#A"
try:
    drive.get(url)

    #Doi 2s cho trang chay
    time.sleep(2)

    #Lay tat ca cac the    "ul"
    ul_tag = drive.find_elements(By.TAG_NAME,"ul")

    #Chon the ul thu 21
    ul_painters = ul_tag[21]

    #Lay ra tat ca the li
    li_tag = ul_painters.find_elements(By.TAG_NAME, "li")

    # Tao danh sach url
    titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tag]
    #Xuat ra danh sach
    for title in titles:
        print(title)
except:
    print("error")



drive.quit()
