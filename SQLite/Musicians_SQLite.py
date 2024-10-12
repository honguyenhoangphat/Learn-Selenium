from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
import sqlite3

#0: TAO CSDL
conn = sqlite3.connect('musicians.db')
c = conn.cursor()
try:
    c.execute('''
        CREATE TABLE musicians (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_name text,
        year_active text,
        )
    ''')
except Exception as e:
    print(e)

def add(band_name, year_active):
    conn = sqlite3.connect('musicians.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO musicians(band_name, year_active)
        VALUES (:band_name, :year_active)
    ''',
              {'band_name': band_name, 'year_active': year_active})
    conn.commit()
    conn.close()

######################################################
# I. Tạo nơi chứa links và tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'Name of the band': [], 'Year active': []})
######################################################
# II. Lấy ra tất cả các đường dẫn để truy cập
# Khởi tạo Webdriver
driver = webdriver.Chrome()
url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
driver.get(url)
# Đợi  để trang tải
try:
    time.sleep(2)

    # Lấy ra tất cả ul
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    #print(len(ul_tags))

    # Chọn thẻ ul thứ 22
    ul_music = ul_tags[21]  # list start with index=0

    # Lấy tất cả các thẻ <li>
    li_tags = ul_music.find_elements(By.TAG_NAME, "li")

    # Tao danh sach cac url
    links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
    for x in links:
        print(x)
except:
    print("Error!")
######################################################
# III. Lay thong tin tung nhac si
urll = driver.get(links[0])
urll_tags = driver.find_elements(By.TAG_NAME, "ul")

ul_music = urll_tags[21]
li1_tags = ul_music.find_elements(By.TAG_NAME, "li")

music_links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li1_tags]
for link1 in all_links:
    try:
        print(link1)
        url = link1
        driver.get(url)
        time.sleep(2)
        try:
            band_name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            band_name = ""
        try:
            years_active = driver.find_element(By.XPATH, "//th[span[text()='Years active']]/following-sibling::td]")
            years_active = years_active.text
        except:
            years_active = ""
            # Tao dictionary thong tin cua hoa si

        add(band_name, years_active)
    except:
        print("Error!!!")

driver.quit()