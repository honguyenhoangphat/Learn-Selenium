#Lấy ra tất cả các họa sĩ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re


#I. Tao dataframe rong~ va tao noi chua link
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': [] })
#
driver = webdriver.Chrome()


## II. Lay ra tat ca hoa si (Bai 4)
for i in range(69, 73):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        driver.get(url)

        #Doi 2s cho trang chay
        time.sleep(3)

        #Lay tat ca cac the    "ul"
        ul_tags = driver.find_elements(By.TAG_NAME,"ul")

        #Chon the ul thu 21
        ul_painters = ul_tags[20]

        #Lay ra tat ca the li
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tao danh sach url
        links = [tag.find_element(By.TAG_NAME, 'a').get_attribute("href") for tag in li_tags]

        all_links.append(links)
        for link in links:
            print(link)
        #Xuat ra danh sach

    except Exception as e:
        print(f"error while fetching painters: {e}")

#III. Lay thong tin tung hoa si mot


#Lay ten hoa si
    try:
        #Khoi tao webdriver
        #driver = webdriver.Chrome()
        #Mo trang
        url = link
        driver.get(url)
        time.sleep(3)
        #Lấy tên họa sĩ


        try:

            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""




        #Lay ngay sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]


        except:
            birth = ""

        #Lay ngay DEAD
        death = ""
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]

        except:
            death = ""


        #Lay QUOC GIA
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text

        except:
            nationality = ""
    except:
        pass
#Tao dictionary thong tin cua hoa si
    painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality }

            #Chuyen doi dictionary thanh DataFrame
    painter_df = pd.DataFrame([painter])

            #Thêm thong tin vao DataFrame chinh
    d = pd.concat([d, painter_df], ignore_index=True)



driver.quit()

#IV. In thong tin
print(d)
#In file excel
data = 'ppaints.xlsx'

#saving the excel

#d.to_excel(file_name)
#print("In ra fle excel thanh cong")
d.to_excel(data,)
print("In ra file excel thành công")
