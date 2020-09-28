import time
import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

n=1
base_url= "https://series.naver.com/novel/categoryProductList.nhn?categoryTypeCode=all&page={}"
Flag = True

while True:
    url = base_url.format(n)
    driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(url)
    #print("Page = " +str(n))
    bs_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")

    #for i in range(25)
    f_container = bs_obj.find('div', {'class', 'lst_thum_wrap'})
    container = f_container.findAll('h3')

    for h3 in container:
        f_title = h3.find('a').attrs['title']
        #if '[독점]' in f_title:
        #    title = f_title.replace("[독점]","")
        #elif '[선공개]' in f_title:
        #    title = f_title.replace("[선공개]","")
        #elif '[단행본]' in f_title:
        #    title = f_title.replace("[단행본]", "")
        #elif '[개정판]' in f_title:
        #    title = f_title.replace("[개정판]", "")
        #elif '[외전]' in f_title:
        #    title = f_title.replace("[외전]", "")
        #elif '[무료연재]' in f_title:
        #    title = f_title.replace("[무료연재]", "")
        #else:
        #    title = f_title
        print(title)

    n = n+1