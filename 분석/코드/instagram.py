# 코드 제작자 및 모듈화 : 한승주 2015722084

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import urllib.request
import warnings # 경고메세지 제거
import requests
from datetime import datetime, timedelta
import pandas as pd
import re

def cleaned(term):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', term)
    return text

# 중복 제거
def duplicate(my_list):
    my_set = set(my_list) # 집합으로 변환
    new_list = list(my_set) # 리스트로 변환
    return new_list

def ig_login(driver):
    warnings.filterwarnings(action='ignore') # 경고 메세지 제거

    # 로그인 계정 정보 [ID : dawaplease / PWD : dawa20152017]
    #ig_id = 'dawaplease'
    #ig_pwd = 'dawa20152017'

    # 로그인 [ID : dawaplease / PW : dawa20152017]
    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(1)

    id_input = driver.find_elements_by_css_selector('#loginForm > div > div > div > label > input')[0]

    id_input.send_keys('dawaplease') # ID 입력
    password_input = driver.find_elements_by_css_selector('#loginForm > div > div > div > label > input')[1]
    password_input.send_keys('dawa20152017') # PW 입력
    password_input.submit()
    time.sleep(3)

def ig_scraping(driver, search_key):
    # 작품 검색
    search_key=cleaned(search_key).replace(" ","")
    print(search_key+" 검색 시작\n")
    search_ig = "https://www.instagram.com/explore/tags/" + search_key + "/"

    # 작품 검색 페이지 로드
    driver.get(search_ig)
    time.sleep(3) #웹 페이지 로드 시간 : 3초

    # 마지막 결과까지 스크롤
    SCROLL_PAUSE_TIME = 1.0
    post_list = []

    # 포스트 링크 추출
    while True:
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        for link1 in soup.find_all(name="div",attrs={"class":"Nnq7C weEfm"}):
            for num in range(3):
                try:
                    title = link1.select('a')[num]
                    real = title.attrs['href']
                    post_list.append(real)
                except:
                    break

        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            else:
                last_height = new_height
                continue

    post_list = duplicate(post_list) # 중복포스트 제거
    post_num = len(post_list) # 검색 결과 개수
    print("총 "+str(post_num)+"개의 데이터.\n")

    # 포스트 데이터 추출
    csvtext = []

    for i in range(0, post_num):
        csvtext.append([])
        post_url = 'https://www.instagram.com'+ post_list[i]
        driver.get(post_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        # 내용
        try:
            content = soup.select('div.C4VMK > span')[0].text
        except:
            content = ''
        csvtext[i].append(content)
        print(content)

        # 작성날짜
        try:
            date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
        except:
            date = ''
        csvtext[i].append(date)
        print(date)

    print(post_num, "개의 데이터 받아오는 중.\n")
    total=post_num
    print("저장 완료.\n")
    
    return csvtext
    # 총 수집 개수 : total | 수집 내용 csvtext [list 타입]