# 코드 제작자 : 조예슬 2017202067
# 코드 모듈화 및 수정 : 한승주 205722084

import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse
import time

def naver_comments(driver, url):
    driver.get(url)
    time.sleep(0.5)

    close_w = driver.find_element_by_css_selector('#eventLayer > div > div > a.lk_close')
    close_w.click()
    time.sleep(0.5)

    comm = driver.find_element_by_css_selector("#ct > div.end_section2 > div:nth-child(2) > a")
    comm.click()
    time.sleep(0.5)

    # 더보기 마지막까지 클릭
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[6]/a/span').click()
            time.sleep(0.5)
        except:
            break

    time.sleep(1)

    reviews = []
    total=len(driver.find_elements_by_class_name('u_cbox_area'))
    for content in driver.find_elements_by_class_name('u_cbox_area'):
        review = content.find_element_by_class_name('u_cbox_contents').text
        date = content.find_element_by_class_name('u_cbox_date').get_attribute('data-value')[:10]
        reviews.append([date, review])
        print(date, review)
    # total : 총 댓글 수 | reviews[type: list]
    
    return reviews