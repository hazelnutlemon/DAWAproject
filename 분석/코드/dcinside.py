# 코드 제작자 : 조예슬 2017202067
# 코드 모듈화 및 수정 : 한승주 205722084

import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse
import re

def cleaned(tmp):
    tmp = re.sub('[^A-Za-z0-9ㄱ-ㅣ가-힣]', '', tmp) # 특수문자로 인한 검색 실패 대비 영어, 한국어, 숫자를 제외한 모든 글자 삭제
    return tmp

def dc_scraping(driver, search):
    search = cleaned(search)
    
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
                        title = soup.head.find("meta", {"name": "title"}).get('content').split("-")[0]
                        date = soup.find('span', class_='gall_date')
                        date = date.get("title")[0:10]
                        content= driver.find_element_by_xpath('// *[ @ id = "container"] / section / article[2] / div[1] / div / div[1] / div[1]').text
                        #print("title " + title + " | date "+ date)
                        # print("content " + content)

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
                    except:
                        continue
            except:
                continue
        n = n+1 # 검색 결과 다음페이지로 이동하기 위한 변수
        
    return dcinside