# 리디북스, 조아라, 트위터, 인스타그램 코드 제작자 및 8개 플랫폼 모듈화를 위한 수정과 모듈화 : 한승주 2015722084 , 김성종 2015722083
# 디씨인사이드, 인스티즈, 네이버 웹소설, 시리즈온 댓글 코드 제작자 : 조예슬

import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib import parse
import time
import bs4
import twint
import re
import nest_asyncio
from urllib.parse import urlparse
import os
import urllib.request
import warnings # 경고메세지 제거
from datetime import datetime, timedelta
import datetime

# 리디북스 로그인
def ridi_login(driver):
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

# 리디북스 댓글 수집
def ridi_comments(select_date,driver, url):
    collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    review_data = []

    driver.get(url)
    # 서비스 종료로 인한 오류 발생 시
    try:
        # 전체 댓글 버튼 클릭
        driver.find_element_by_xpath('//*[@id="review_list_section"]/div[1]/ul[1]/li[2]/a').click()
        time.sleep(1)
        ## 공감순 버튼 클릭
        #driver.find_element_by_xpath('//*[@id="review_list_section"]/div[1]/ul[2]/li[2]/a').click()
        #time.sleep(1)
    except:
        return review_data
    
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
    count=0
    for review in reviews:
        date = review.find('li',class_='review_date').text
        date=date.replace(" ","")
        date=date.replace(".","-")[0:10]
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        if(date_obj.year<2020):
            #print("2020년 댓글 아님.")
            continue
        if(date_obj.day not in select_date):
            #print("표본 x")
            continue
        if(collect_check[date_obj.month-1]>=100):
            continue
        #print(date)

        if (review.find('span',class_='hidden')==None):
            comment=review.find('p',class_='review_content js_review_content').text
        else:
            comment=review.find('span',class_='hidden').text
        #print(comment)
        collect_check[date_obj.month-1]+=1
        review_data.append([date, comment])
        if(collect_check.count(100)==10):
            break
        count+=1
        if(count>3000):
            break
            
    return review_data

    # 총 댓글 수 total | review_data [type: list]

# 조아라 댓글
def joara_comments(driver, url):
    collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    review_data = []
    
    driver.get(url+"&book_dtype=comment_premium")
    time.sleep(1)
    try:
        driver.current_url
    except:
        return review_data
    
    # 더보기 버튼 클릭하기
    while True:
        try:
            html = driver.page_source
            if(BeautifulSoup(html, 'html.parser').select('#comment_list')[0].find_all(name="dd")[-1].find('span',class_='date').text[0:4]<"2020"):
                break
            more_btn = driver.find_element_by_css_selector('#commentMoreBtn > a')
            more_btn.click()
            time.sleep(1)

        except:
            break      

    # 댓글 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    comment_list = soup.select('#comment_list')

    comments = comment_list[0].find_all(name="dd")

    for comment in comments:
        date = comment.find('span',class_='date').text[0:10]
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        if(date_obj.year<2020):
            #print("2020년 댓글 아님.")
            continue
        #if(date_obj.day not in select_date):
            #print("표본 x")
        #    continue
        #if(collect_check[date_obj.month-1]>=100):
        #    continue
        #print(date)

        review=comment.find('p',class_='comment').text
        #print(review)
        #collect_check[date_obj.month-1]+=1
        review_data.append([date, review])
        #if(collect_check.count(100)==10):
        #    break
        

    return review_data

    # 총 댓글 수 total | review_data [type: list]
    
# 네이버 로그인
def naver_login(driver):
    naver_id = "shung2rhea"
    naver_pw = "rhea155204"
    driver.get('https://nid.naver.com/nidlogin.login')
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + naver_id + "\'")
    # time.sleep(1)
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + naver_pw + "\'")
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    time.sleep(0.5) ## 0.5초
    
# 네이버 웹소설 댓글
def naver_comments(driver, url):
    #collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    reviews = []
    
    driver.get(url)
    time.sleep(0.5)
    # 삭제된 링크 접속으로 인한 오류 해결 구문 추가
    try:
        comm = driver.find_element_by_css_selector("#ct > div.end_section2 > div:nth-child(2) > a")
        comm.click()
        time.sleep(1)
    except:
        return reviews
    # 더보기 마지막까지 클릭
    while True:
        try:
            # 현재 마지막 댓글이 2020년 이전 댓글일 경우 아래 더보기 그만 누르기
            if(driver.find_elements_by_class_name('u_cbox_comment_box')[-1].find_element_by_class_name('u_cbox_date').get_attribute('data-value')[:4]<"2020"):
                break
            driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[6]/a').click()
            time.sleep(0.5)
        # 마지막 댓글이 블라인드 댓글이거나 혹은 댓글이 0인 경우
        except:
            try:
                # 현재 마지막 댓글이 "신고로 인해 임시 블라인드 되었습니다."인 경우 더보기 누르기
                if(driver.find_elements_by_class_name('u_cbox_comment_box')[-1].find_element_by_class_name('u_cbox_delete_contents')):
                    driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[6]/a').click()
                    time.sleep(0.5)
                    continue
            # 댓글이 0인 경우는 빈 리스트 리턴
            except:
                break
            break

    for content in driver.find_elements_by_class_name('u_cbox_comment_box'):
        try:
            date = content.find_element_by_class_name('u_cbox_date').get_attribute('data-value')[:10]
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            #print(date)
            if(date_obj.year<2020):
                #print("2020년 댓글 아님.")
                continue
            #if(date_obj.day not in select_date):
            #    #print("표본 x")
            #    continue
            #if(collect_check[date_obj.month-1]>=100):
            #    continue
            review = content.find_element_by_class_name('u_cbox_contents').text
            #collect_check[date_obj.month-1]+=1
            reviews.append([date, review])
            #if(collect_check.count(100)==10):
            #    break
        except:
            continue
    
        #print(date, review)
    # total : 총 댓글 수 | reviews[type: list]
    #print(collect_check)
    return reviews

# 네이버 시리즈온 댓글
def serieson_comments(select_date, driver, url):
    collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    serieson_reviews = []

    # 서비스 중단 작품 에러 발생 대비
    try:
        driver.get(url)
        time.sleep(0.5)
        
        driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[1]/div[2]/ul/li[2]/a').click()
        time.sleep(2)
    except:
        return serieson_reviews

    count=0
    flag=True
    while True:
        try:        
            for li in driver.find_elements_by_class_name('u_comment_depth'):
                date = li.find_element_by_class_name('u_comment_info').text[-21:-11]
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                
                count += 1
                if(count>7000):
                    flag=False
                    break
                if(date_obj.year<2020):
                    #print("2020년 댓글 아님.")
                    continue
                if(date_obj.day not in select_date):
                    #print("표본 x")
                    continue
                if(collect_check[date_obj.month-1]>=100):
                    continue
                comment = li.find_element_by_class_name('u_comment_text').text
                serieson_reviews.append([date, comment])
                collect_check[date_obj.month-1]+=1
                
                
            if(flag==False):
                break
            if(date_obj.year<2020):
                #print("2020년 댓글 아님.")
                break
            driver.find_element_by_xpath('//*[@id="comment_module"]/div[5]/div/a[2]').click()
            time.sleep(1)
        except:
            break
            
    #print(collect_check)
    return serieson_reviews

# 트위터
# 특수 문자 제거 : 숫자, 영어, 한글을 제외 모든 글자 지우기
def clean_name(term):
    cleaned = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', '', term) # 특수문자 제거
    return cleaned

def tweet_clean(tweet_text):
    # URL 제거 시도했으나 경우의 수가 많아 패스. 분석에서 연관성 확인 과정에서 안나오지 않을까
    pattern = 'pic.twitter.com/[a-zA-Z0-9]+'
    tweet_text = re.sub(pattern=pattern, repl='',string=tweet_text) # pic.twitter.com/XXXXXXX 사진 링크 삭제
    return tweet_text

def tweet_scraping(search):
    nest_asyncio.apply() # Runtime Error 발생하는 경우를 대비 - 코드 휴식을 위한 추가 코드
    
    tweets = []
    
    # 검색 시작 : 2020-01-01 / 끝 : 2020-09-30
    since = "2020-01-01"
    until = "2020-09-30"
    
    # Twint를 이용한 트위터 검색 결과
    c = twint.Config()
    
    # 파라미터 설정
    c.Search = search
    c.Since = since
    c.Until = until
    c.Popular_tweets = True
    c.Store_object = True
    c.Store_object_tweets_list = tweets
    c.Hide_output = True
    
    twint.run.Search(c) # 트윗 수집 시작
    tweet_data = [] # 수집한 트위터를 list 타입으로 저장
    
    for tweet in tweets:
        date = tweet.datestamp # YYYY-MM-DD 형식으로 작성 날짜 저장
        tweet_text = tweet_clean(tweet.tweet) # 트윗 내용 저장
        tweet_data.append([date,tweet_text])
        
    #total = len(tweets) # 수집한 트윗 개수는 따로
    #print("2019-01-01부터 2020-09-30까지 총 트윗 개수 : ", total)
    # tweet_data = 수집한 트윗과 작성 날짜 [리스트 타입]
    
    return tweet_data

# 인스타그램
# 특수문자제외 해시태그 검색 가능 형식으로 변경
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
    collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    
    # 작품 검색
    search_key=cleaned(search_key).replace(" ","")
    print(search_key+" 검색 시작\n")
    search_ig = "https://www.instagram.com/explore/tags/" + search_key + "/"

    # 작품 검색 페이지 로드
    driver.get(search_ig)
    time.sleep(3) #웹 페이지 로드 시간 : 3초

    # 마지막 결과까지 스크롤
    SCROLL_PAUSE_TIME = 2.5
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
        if(len(post_list)>100):
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
        post_url = 'https://www.instagram.com'+ post_list[i]
        driver.get(post_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        # 작성날짜
        try:
            date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            #print(date)
            if(date_obj.year<2020):
                #print("2020년 댓글 아님.")
                continue
            if(date_obj.day not in select_date):
                #print("표본 x")
                continue
            if(collect_check[date_obj.month-1]>=100):
                continue
        except:
            date = ''
        #csvtext.append([])
        #csvtext[i].append(date)

        # 내용
        try:
            content = soup.select('div.C4VMK > span')[0].text
        except:
            content = ''
        #csvtext[i].append(content)
        #collect_check[date_obj.month-1]+=1
        csvtext.append([date, content])
        #if(collect_check.count(100)==10):
        #    break
        
        #print(content)
        #print(date)

    #print(post_num, "개의 데이터 받아오는 중.\n")
    #print(collect_check)
    #print("저장 완료.\n")
    
    return csvtext
    # 총 수집 개수 : total | 수집 내용 csvtext [list 타입]
    
# 디씨인사이드
def cleaned_dc(tmp):
    tmp = re.sub('[^A-Za-z0-9ㄱ-ㅣ가-힣]', '', tmp) # 특수문자로 인한 검색 실패 대비 영어, 한국어, 숫자를 제외한 모든 글자 삭제
    return tmp

def dc_scraping(driver, search):
    collect_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월]
    
    search = cleaned_dc(search)
    
    n = 1
    pre_tit = None
    n_url = "https://search.dcinside.com/post/p/{}"
    nm_url = "/sort/latest/q/" + parse.quote(search)
    Flag = True
    pre_tit = None

    dcinside = [] # 수집 결과 저장 리스트

    while True:
        m_url = n_url.format(n)
        s_url = m_url + nm_url
        req = requests.get(s_url) # 검색 페이지 오픈

        source = req.content
        bs_obj = BeautifulSoup(source, "html.parser")

        f_container = bs_obj.find('ul', {'class', 'sch_result_list'})

        #print(s_url)

        tit = f_container.find('a', {'class', 'tit_txt'}) # 현재 페이지

        # 현재페이지와 이전 페이지가 같다면 루프 종료.
        if pre_tit == tit:
            break
        pre_tit = tit

        con = f_container.findAll('li')
        for li in con:
            # 게시글 삭제로 인한 에러가 나올 경우 패스.
            try:
                s_url = li.find('a').attrs['href'] # 게시글 링크 가져오기
                driver.get(s_url)

                soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
                # 성인 페이지 넘어가기
                if "성인인증" in soup.find('h2').text:
                    continue

                else:
                    # 게시글 삭제로 인한 에러가 나올 경우 패스.
                    try:
                        # title : 제목, date : 작성 날짜, content : 작성 내용 + 댓글.
                        date = soup.find('span', class_='gall_date')
                        date = date.get("title")[0:10]
                        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                        if(date_obj.year<2020):
                            #print("2020년 댓글 아님.")
                            break
                        #if(date_obj.day not in select_date):
                            #print("표본 x")
                        #    continue
                        #if(collect_check[date_obj.month-1]>=100):
                        #    continue
                        title = soup.head.find("meta", {"name": "title"}).get('content').split("-")[0]
                        
                        content= driver.find_element_by_xpath('// *[ @ id = "container"] / section / article[2] / div[1] / div / div[1] / div[1]').text
                        #print("title " + title + " | date "+ date)
                        # print("content " + content)
                        if search.replace(" ", "") not in content.replace(" ", ""):
                            continue
                        comment = soup.find('div', {'class', 'comment_box'})
                        # 댓글이 없을 경우 댓글 패스.
                        if comment == None:
                            continue
                        else:
                            reviews=""
                            com_2 = comment.findAll('p')
                            # 댓글을 모두 작성 내용에 합치기.
                            for review in com_2:
                                reviews=reviews+review.text+" "
                            # print(reviews)
                        dcinside.append([date, title, content + " " + reviews])
                        #collect_check[date_obj.month-1]+=1
                        #if(collect_check.count(100)==10):
                        #    break
                    except:
                        continue
            except:
                continue
        n = n+1# 검색 결과 다음페이지로 이동하기 위한 변수
        if(n>5):
            break
    #print(collect_check)
    return dcinside


def tistory_crawling(search_name):
    session = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    tmp = search_name + " 리뷰"  # 혹은 후기
    base_url = "https://search.daum.net/search?w=blog&nil_search=btn&DA=STC&enc=utf8&q=" + parse.quote(
        tmp) + "&f=section&SA=tistory&page={}"
    n = 1
    pre_page = None
    search_name=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', search_name)
    # initialize
    info_lists = []

    while True:
        url = base_url.format(n)
        r = requests.get(url)
        c = r.content
        html = bs4.BeautifulSoup(c, "html.parser")

        main = html.find('div', {'class', 'type_fulltext wid_n'})

        count = html.find('span', {'class', 'txt_info'})
        if (count == None):
            #print("프로그램 종료합니다")
            break
        page = count.text.split(" /")[0]
        if (pre_page == page):
            #print("프로그램 종료합니다")
            break
        pre_page = page
        
        n = n + 1
        if(n>10):
            break
        main = html.find('div', {'class', 'type_fulltext wid_n'})
        coll = main.find('div', {'class', 'coll_cont'})
        ul = coll.find('ul')
        li_s = ul.findAll('li')

        for li in li_s:
            href = li.find('a').attrs['href'].replace(".com/", ".com/m/")
            if 'tistory' not in href:
                continue
            r = session.get(href, headers=header)
            html = bs4.BeautifulSoup(r.content, "html.parser")

            title = html.find('h2', {'class', 'tit_blogview'}).text
            title=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', title)
            if search_name.replace(" ", "") not in title.replace(" ", ""):
                continue
            #print("제목 : " + title)

            author = html.find('span', {'class', 'txt_by'}).text
            #print("작성자 : " + author)

            date = html.find('time', {'class', 'txt_date'}).text
            #print("작성일시 : " + date)

            post_area = html.find('div', {'class', 'blogview_content'})

            texts = post_area.findAll('p')
            post = ''
            #print(
            #    "\n----------------------------------------\n" + "게시글\n" + "----------------------------------------\n")
            for text in texts:
                post = post + text.text
            #print(post)
            #print("\n----------------------------------------\n")
            info_list = [title, author, date, post]

            info_lists.append(info_list)

    return info_lists


def naver_crawling(search_name):
    info_lists = []

    session = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    tmp = search_name + " 리뷰"  # 혹은 후기
    search_name=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', search_name)
    base_url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=blog.me&query=" + parse.quote(
        tmp) + "&sm=tab_pge&srchby=all&st=sim&where=post&start={}"
    n = 1
    pre_page = None
    while True:
        url = base_url.format(n)
        r = requests.get(url)
        c = r.content
        html = bs4.BeautifulSoup(c, "html.parser")
        main = html.find('div', {'class', 'blog section _blogBase _prs_blg'})
        count = main.find('span')
        if (count == None):
            #print("프로그램 종료합니다")
            break
        page = count.text.split(" /")[0].replace(" ", "")
        if page=='이블로그제외하고다시검색':
            break
        if (pre_page == page):
            #print("프로그램 종료합니다")
            break
        pre_page = page
        n = n + 10
        if(n>101):
            break
        ul = main.find('ul')
        li_s = ul.findAll('li')

        for li in li_s:
            post = ''
            href = li.find('a').attrs['href']
            if ('blog.naver.com' or 'blog.me') not in href:
                continue
            if 'blog.me' in href:
                part_1 = href.split('.')[0]
                part_2 = href.split('/')[1]
                url = "https://m.blog.naver.com/" + part_1 + "/" + part_2
            else:
                url = href.replace("://", "://m.")
            
            req = session.get(url, headers=header)
            html = bs4.BeautifulSoup(req.text, "html.parser")

            body = html.find('div', {'class', '_postView'})
            if body != None:
                post_area = body.find('div', {'class', 'post_tit_area'})
                if post_area != None:
                    title = post_area.find('h3').text
                    title=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', title)
                    if search_name.replace(" ", "") not in title.replace(" ", ""):
                        continue
                    #print(title)

                    info_area = post_area.find('div', {'class', 'author_area'})
                    author_area = info_area.find('div', {'class', 'se_author'})
                    author = author_area.find('a').find('strong').text
                    #print(author)

                    date = info_area.find('p').text
                    #print(date)

                    content_area = body.find('div', {'class', 'post_ct'})
                    contents = content_area.findAll('p')
                    for content in contents:
                        content = content.text
                        post = post + content
                        #print(content)

                else:
                    post_area = body.find('div', {'class', 'post_ct'})
                    title_area = post_area.find('div', {'class', 'se-viewer se-theme-default'})
                    if title_area != None:
                        info_area = title_area.find('div', {'class', 'se-component-content'})
                        title = info_area.find('div', {'class', 'se-module se-module-text se-title-text'}).find(
                            'p').text
                        title=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', title)
                        if search_name.replace(" ", "") not in title.replace(" ", ""):
                            continue
                        #print(title)

                        author_area = info_area.find('div', {'class', 'blog_authorArea'})
                        author = author_area.find('div', {'class', 'blog_author'}).find('a').find('strong').text
                        #print(author)
                        date = author_area.find('p').text
                        #print(date)

                        content_area = title_area.find('div', {'class', 'se-main-container'})
                        contents = content_area.findAll('p')
                        for content in contents:
                            content = content.text
                            post = post + content
                            #print(content)
                    else:
                        title_area = post_area.findAll('div', {'class', 'se_component_wrap'})[0]
                        title = title_area.find('h3').text
                        if search_name.replace(" ", "") not in title.replace(" ", ""):
                            continue
                        #print(title)

                        info_area = title_area.find('div', {'class', 'blog_authorArea'})
                        author_area = info_area.find('div', {'class', 'blog_author'})
                        author = author_area.find('a').text
                        #print(author)

                        date = info_area.find('p').text
                        #print(date)

                        content_area = post_area.findAll('div', {'class', 'se_component_wrap'})[1]
                        contents = content_area.findAll('p')
                        for content in contents:
                            content = content.text
                            post = post + content
                         #   print(content)
            else:
                body = html.find('div', {'class', 'postListBody'})
                post_area = body.find('div', {'class', 'se-viewer se-theme-default'})
                title_area = post_area.find('div', {'class', 'se-component se-documentTitle se-l-default'})
                title = title_area.find('div', {'class', 'se-module se-module-text se-title-text'}).find('p').text
                title=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', title)
                if search_name.replace(" ", "") not in title.replace(" ", ""):
                    continue
                #print(title)

                author_area = title_area.find('div', {'class', 'blog2_container'})
                author = author_area.find('span').find('a').text
                #print(author)

                date = author_area.find('span', {'class', 'se_publishDate pcol2'}).text
                #print(date)

                content_area = post_area.find('div', {'class', 'se-main-container'})
                contents = content_area.findAll('p')
                for content in contents:
                    content = content.text
                    post = post + content
                 #   print(content)

            info_list = [title, author, date, post]

            info_lists.append(info_list)

    return info_lists


def daum_crawling(search_name):
    flag = True
    session = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    tmp = search_name + " 리뷰"  # 혹은 후기
    base_url = "https://search.daum.net/search?nil_suggest=btn&w=blog&DA=STC&q=" + parse.quote(
        tmp) + "&f=section&SA=daumsec&page={}"
    n = 1
    pre_page = None

    # initialize
    info_lists = []
    search_name=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', search_name)
    while True:
        url = base_url.format(n)
        r = requests.get(url)
        c = r.content
        html = bs4.BeautifulSoup(c, "html.parser")

        main = html.find('div', {'class', 'type_fulltext wid_n'})

        count = html.find('span', {'class', 'txt_info'})
        if (count == None):
           # print("프로그램 종료합니다")
            break
        page = count.text.split(" /")[0]
        if (pre_page == page):
          #  print("프로그램 종료합니다")
            break
        pre_page = page
        n = n + 1
        if(n>10):
            break
        main = html.find('div', {'class', 'type_fulltext wid_n'})
        coll = main.find('div', {'class', 'coll_cont'})
        ul = coll.find('ul')
        li_s = ul.findAll('li')

        for li in li_s:
            href = li.find('a').attrs['href'].replace("://", "://m.")
           # print(href)
            r = session.get(href, headers=header)
            html = bs4.BeautifulSoup(r.content, "html.parser")

            title = html.find('h2', {'class', 'tit_blogview'}).text
            title=re.sub('[^ ㄱ-ㅎ|ㅏ-ㅣ|가-힣a-zA-Z0-9]', '', title)
            if search_name.replace(" ", "") not in title.replace(" ", ""):
                continue
            #print("제목 : " + title)

            author = html.find('span', {'class', 'txt_by'}).text
            #print("작성자 : " + author)

            date = html.find('time', {'class', 'txt_date'}).text
            #print("작성일시 : " + date)

            post_area = html.find('div', {'class', 'blogview_content'})

            texts = post_area.findAll('p')
            post = ''
            #print(
            #    "\n----------------------------------------\n" + "게시글\n" + "----------------------------------------\n")
            for text in texts:
                post = post + text.text

            #print("\n----------------------------------------\n")
            info_list = [title, author, date, post]

            info_lists.append(info_list)

    return info_lists