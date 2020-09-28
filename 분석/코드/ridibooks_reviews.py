# 코드 제작자 및 모듈화 : 한승주 2015722084

import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib import parse
import time

def ridi_login(driver):
    # 로그인 계정 정보
    # ridi_id = 'shung2rhea'
    # ridi_pwd = 'rhea155204'

    # 로그인
    driver.get('https://ridibooks.com/account/login')
    time.sleep(0.5)
    # ID 입력
    ridi_login = driver.find_element_by_id("login_id")
    ridi_login.clear()
    ridi_login.send_keys('shung2rhea') # ID 직접 입력
    # 비밀번호 입력
    ridi_login = driver.find_element_by_id("login_pw")
    ridi_login.clear()
    ridi_login.send_keys('rhea155204') # PW 직접 입력
    # 로그인 버튼 클릭
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/form/button").click()
    time.sleep(1)

def ridi_comments(driver, url):
    # 댓글 크롤링
    driver.get(url)
    time.sleep(1)

    # 전체 댓글 버튼 클릭
    driver.find_element_by_xpath('//*[@id="review_list_section"]/div[1]/ul[1]/li[2]/a').click()
    time.sleep(0.5)

    # 더보기 버튼 클릭
    while True:
        try:
            more_btn = driver.find_element_by_css_selector('#review_list_section > div.review_list_wrapper.js_review_list_wrapper.active > div.more_review_button_wrapper.js_more_review_button_wrapper > button')
            more_btn.click()
            time.sleep(0.5)

        except:
            break

    total = 0

    source = driver.page_source
    soup=BeautifulSoup(source, 'html.parser')

    reviews=soup.select("#review_list_section > div.review_list_wrapper.js_review_list_wrapper.active > ul > li")

    review_data = []

    for review in reviews:
        date = review.find('li',class_='review_date').text
        date=date.replace(" ","")
        date=date.replace(".","-")[0:10]
        #print(date)

        if (review.find('span',class_='hidden')==None):
            comment=review.find('p',class_='review_content js_review_content').text
        else:
            comment=review.find('span',class_='hidden').text
        #print(comment)

        review_data.append([date, comment])
        total += 1

    print("총 댓글 수: ", total)
    return review_data

    # 총 댓글 수 total | review_data [type: list]