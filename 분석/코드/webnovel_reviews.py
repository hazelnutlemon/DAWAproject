import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse
import time

tmp = input("작품제목 : ")
n = 1
total = 0
base_url = "https://m.novel.naver.com/search.nhn?keyword=" + parse.quote(tmp)

maximum = 0
page = 1

driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
driver.get(base_url)
soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

findurl = soup2.find("ul", {"class", "lst_type2"}).find('a').attrs['href']
fin_url = "https://m.novel.naver.com/" + findurl

driver.get(fin_url)
soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

time.sleep(1)
close_w = driver.find_element_by_css_selector('#eventLayer > div > div > a.lk_close')
close_w.click()
time.sleep(1)

time.sleep(1)
comm = driver.find_element_by_css_selector("#ct > div.end_section2 > div:nth-child(2) > a")
comm.click()
time.sleep(1)


while True:
    try:
        driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[6]/a/span').click()
        time.sleep(0.5)
    except:
        break

time.sleep(3)
contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
for content in contents:
    print(content.text)