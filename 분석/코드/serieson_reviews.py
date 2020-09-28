import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse
import time

base_url = "https://m.series.naver.com/novel/detail.nhn?productNo=5204313"

driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
driver.get(base_url)
soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

time.sleep(1)
comm = driver.find_element_by_css_selector("#ct > div.nstore_open > div.nstore_rental > div.content_activity > ul > li:nth-child(2) > a")
comm.click()
time.sleep(1)

maximum = 0
page = 1

time.sleep(3)

while True:
    try:
        contents = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[1]/p')
        contents2 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[2]/p')
        contents3 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[3]/p')
        contents4 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[4]/p')
        contents5 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[5]/p')
        contents6 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[6]/p')
        contents7 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[7]/p')
        contents8 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[8]/p')
        contents9 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[9]/p')
        contents10 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[10]/p')
        contents11 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[11]/p')
        contents12 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[12]/p')
        contents13 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[13]/p')
        contents14 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[14]/p')
        contents15 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[15]/p')
        contents16 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[16]/p')
        contents17 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[17]/p')
        contents18 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[18]/p')
        contents19 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[19]/p')
        contents20 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[20]/p')
        contents21 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[21]/p')
        contents22 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[22]/p')
        contents23 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[23]/p')
        contents24 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[24]/p')
        contents25 = driver.find_elements_by_xpath('//*[@id="comment_module"]/ul/li[25]/p')

        for content in contents:
            print(content.text)
        for content in contents2:
            print(content.text)
        for content in contents3:
            print(content.text)
        for content in contents4:
            print(content.text)
        for content in contents5:
            print(content.text)
        for content in contents6:
            print(content.text)
        for content in contents7:
            print(content.text)
        for content in contents8:
            print(content.text)
        for content in contents9:
            print(content.text)
        for content in contents10:
            print(content.text)
        for content in contents11:
            print(content.text)
        for content in contents12:
            print(content.text)
        for content in contents13:
            print(content.text)
        for content in contents14:
            print(content.text)
        for content in contents15:
            print(content.text)
        for content in contents16:
            print(content.text)
        for content in contents17:
            print(content.text)
        for content in contents18:
            print(content.text)
        for content in contents19:
            print(content.text)
        for content in contents20:
            print(content.text)
        for content in contents21:
            print(content.text)
        for content in contents22:
            print(content.text)
        for content in contents23:
            print(content.text)
        for content in contents24:
            print(content.text)
        for content in contents25:
            print(content.text)

        next = driver.find_element_by_css_selector('#comment_module > div.__comment_page_area > div > a.u_pg2_btn.u_pg2_next.__comment_page_next')
        next.click()
        time.sleep(0.5)
    except:
        break




