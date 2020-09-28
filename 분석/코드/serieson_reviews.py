import bs4
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

#print(soup3)

while True:
    try:
        driver.get(driver.current_url)
        #print(driver.current_url)
        soup3 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        temp = soup3.find('div', {'class', 'u_comment_box u_comment_v2'})
        con = temp.findAll('li')
        #print(con)

        for li in con:
            date = li.find('div', {'class', 'u_comment_info'})
            for tag in date.find_all(['em','span','a']):
                tag.replace_with('')
            date_p = date.text
            print(date_p)
            comment = li.find('p', {'class', 'u_comment_text u_comment_txt1'})
            com_p = comment.text
            print(com_p)

        next = driver.find_element_by_css_selector('#comment_module > div.__comment_page_area > div > a.u_pg2_btn.u_pg2_next.__comment_page_next')
        next.click()
        time.sleep(0.5)
    except:
        break




