# 코드 제작자 : 조예슬
# 현재 버전 코드 수정자 : 김성종

#!/usr/bin/env python
# coding: utf-8

# In[7]:


import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse

def hasxpath(xapth):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

url="https://www.instiz.net/m/index.htm?welcome=1"
#https://www.instiz.net/name_enter/74027774
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)
try:
    driver.find_element_by_xpath.click('/html/body/div[8]/div/div[4]').click()
except:
    pass

url="https://www.instiz.net/name_enter/74027774"
driver.get(url)

req = requests.get(url)
source = req.content

soup = BeautifulSoup(source, "html.parser")
#print(soup)
title = soup.head.find("meta", {"property": "og:title"}).get('content')
content = soup.head.find("meta", {"name": "description"}).get('content')
date = soup.head.find("meta", {"name": "description"}).get('content')
date = date[0:13]
count = soup.find('a', {'class', 'cmt'})
con2 = soup.find('div', {'class', 'memo_content'})
print(title, date)
print(count.text)
print(con2.text)
try:
    temp=driver.find_element_by_xpath('//*[@id="ajax_table"]/tbody/tr[1]/td[2]/div[2]').text.replace('•••답글','')
    print(temp)
    

except:
    pass


# In[ ]:




