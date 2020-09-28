# 코드 제작자 : 조예슬
# 수정 : 한승주

import bs4
from selenium import webdriver
from urllib import parse
import time

# 네이버 로그인
def login(driver):
    naver_id = "네이버 아이디 입력"
    naver_pw = "네이버 비밀번호 입력"
    driver.get('https://nid.naver.com/nidlogin.login')
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + naver_id + "\'")
    # time.sleep(1)
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + naver_pw + "\'")
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    time.sleep(0.5) # 0.5초 wait

base_url = "https://m.series.naver.com/novel/detail.nhn?productNo=5204313"

driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe') # 크롬 드라이버 실행
driver.get(base_url)
soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

time.sleep(1)
comm = driver.find_element_by_css_selector("#ct > div.nstore_open > div.nstore_rental > div.content_activity > ul > li:nth-child(2) > a")
comm.click()
time.sleep(1)

maximum = 0
page = 1

time.sleep(3)

serieson_reviews = []
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
            date_p = date.text[1:11]
            comment = li.find('p', {'class', 'u_comment_text u_comment_txt1'})
            com_p = comment.text
            serieson_reviews.append([date_p, com_p])

        next = driver.find_element_by_css_selector('#comment_module > div.__comment_page_area > div > a.u_pg2_btn.u_pg2_next.__comment_page_next')
        next.click()
        time.sleep(0.5)
    except:
        break