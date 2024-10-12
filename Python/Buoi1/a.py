from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

# I. Tạo dataframe rỗng và tạo nơi chứa link
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khởi tạo webdriver
driver = webdriver.Chrome()

# II. Lấy ra tất cả họa sĩ (Bài 4)
for i in range(65, 92):
    url = f"https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22{chr(i)}%22"
    try:
        driver.get(url)
        time.sleep(3)

        # Lấy tất cả các thẻ "ul"
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(f"Number of <ul> tags found: {len(ul_tags)}")

        # Kiểm tra xem có đủ thẻ ul không
        if len(ul_tags) > 20:
            ul_painters = ul_tags[20]
            li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

            # Tạo danh sách url
            links = [tag.find_element(By.TAG_NAME, 'a').get_attribute("href") for tag in li_tags]
            all_links.extend(links)

    except Exception as e:
        print(f"Error while fetching painters: {e}")

# III. Lấy thông tin từng họa sĩ
for link in all_links:
    print(link)
    try:
        driver.get(link)
        time.sleep(2)

        # Lấy tên họa sĩ
        name = driver.find_element(By.TAG_NAME, "h1").text

        # Lấy ngày sinh
        birth = ""
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', birth)
            birth = birth[0] if birth else ""
        except:
            pass

        # Lấy ngày chết
        death = ""
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]+\s+[A-Za-z]+\s+[0-9]{4}', death)
            death = death[0] if death else ""
        except:
            pass

        # Lấy quốc gia
        nationality = ""
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            pass

        # Tạo dictionary thông tin của họa sĩ
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}
        painter_df = pd.DataFrame([painter])

        # Thêm thông tin vào DataFrame chính
        d = pd.concat([d, painter_df], ignore_index=True)

    except Exception as e:
        print(f"Error while fetching painter info: {e}")

# Đóng webdriver
driver.quit()

# IV. In thông tin
print(d)

# In file excel
file_name = 'Paint.xlsx'
d.to_excel(file_name, index=False)
print("In ra file excel thành công")
