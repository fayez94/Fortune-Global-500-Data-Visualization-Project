from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


columns = ['Rank', 'Name', 'Revenue', 'Revenue in percentage', 'Profit', 'Profit in percentage', 'Assets', 'employees', 'Change in rank', 'years on global 500 list' ]


def get_company_details(td_text):
    contents = {}
    contents["Rank"] = td_text[0]
    contents["Name"] = td_text[1]
    contents["Revenue"] = td_text[2]
    contents["Revenue in percentage"] = td_text[3]
    contents["Profit"] = td_text[4]
    contents["Profit in percentage"] = td_text[5]
    contents["Assets"] = td_text[6]
    contents["employees"] = td_text[7]
    contents["Change in rank"] = td_text[8]
    contents["years on global 500 list"] = td_text[9]
    return contents

all_info = []
driver = webdriver.Chrome()
url = "https://fortune.com/ranking/global500/"
driver.get(url)

def table_data_one_time():
    full_tbl = driver.find_element(By.CLASS_NAME, "sc-617fa5cf-1")
    rows = full_tbl.find_elements(By.TAG_NAME, "tr")
    for idx, row in enumerate(rows[1:]):
        cells = row.find_elements(By.TAG_NAME, "td")
        td_text = [td.text for td in cells]
        all_info.append(get_company_details(td_text[:-1]))
    # driver.close()
    return 


#for all pages
nxt_btn = driver.find_element(By.XPATH, "//button[@data-cy='filter-next-page']")   #// for tag name; @ for attribute 
total_pg = driver.find_element(By.XPATH, "//span[@class='page-number']")

total_pg = int(total_pg.text.split()[-1])
# print(total_pg)

for i in range(0, total_pg):
    table_data_one_time()
    driver.execute_script("arguments[0].click();", nxt_btn)    #for click purpose 

print(len(all_info))
    

df = pd.DataFrame(data = all_info, columns = columns)
df.to_csv("best_Commpany_details_USA.csv", index=False)


# if __name__ == '__main__':
#     main()