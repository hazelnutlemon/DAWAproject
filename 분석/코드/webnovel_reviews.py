import time
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from urllib import parse
import time

n = 101
Flag = True
title_list = []
total = 0
pre_title=None
while True:
    if n == 101:

        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=101&page={}"

        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)

        Flag = True
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")
            #print(bs_obj)

            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_rom'})
            title = f_container.find('li').find('a').attrs['title']
            if pre_title == title:
                print(n)
                n = n + 1
                break
            pre_title=title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i + 1

    elif n == 102:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=102&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        Flag = True
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")
            #print(bs_obj)

            #print(url)
            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_fan'})
            #print(f_container)
            title = f_container.find('li').find('a').attrs['title']
            if pre_title == title:
                print(n)
                n = n + 1
                break
            pre_title = title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i + 1

    elif n == 103:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=103&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        Flag = True
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_hro'})
            title = f_container.find('li').find('a').attrs['title']
            if pre_title == title:
                print(n)
                n = n + 1
                break
            pre_title = title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i + 1

    elif n == 104:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=104&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_mth'})
            title = f_container.find('li').find('a').attrs['title']
            if pre_title == title:
                print(n)
                n = n + 1
                break
            pre_title = title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i + 1

    elif n == 105:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=105&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            if 'list_type1 v2 NE=a:lst_his' in bs_obj:
                f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_his'})
                title = f_container.find('li').find('a').attrs['title']
                if pre_title == title:
                    print(n)
                    n = n + 1
                    break
                pre_title = title
                con = f_container.findAll('li')

                for li in con:
                    title_list.append([])
                    f_title = li.find('a').attrs['title']
                    f_url = li.find('a').attrs['href']
                    title_list[total].append(f_title)
                    title_list[total].append("https://m.novel.naver.com/"+f_url)
                    title_list[total].append('네이버 웹소설')
                    print(f_title)
                    print(f_url)
                    total = total + 1

                i = i + 1
            else:
                n = n + 1
                break



    elif n == 106:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=106&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            if 'list_type1 v2 NE=a:lst_lno' in bs_obj:
                f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_lno'})
                title = f_container.find('li').find('a').attrs['title']
                if pre_title == title:
                    print(n)
                    n = n + 1
                    break
                pre_title = title
                con = f_container.findAll('li')

                for li in con:
                    title_list.append([])
                    f_title = li.find('a').attrs['title']
                    f_url = li.find('a').attrs['href']
                    title_list[total].append(f_title)
                    title_list[total].append("https://m.novel.naver.com/" + f_url)
                    title_list[total].append('네이버 웹소설')
                    print(f_title)
                    print(f_url)
                    total = total + 1

                i = i + 1
            else:
                n = n + 1
                break


    elif n == 107:
        print(n)
        n = n + 1

    elif n == 108:
        print(n)
        n = n + 1

    elif n == 109:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=109&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_rof'})
            title = f_container.find('li').find('a').attrs['title']
            if pre_title == title:
                print(n)
                n = n + 1
                break
            pre_title = title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i + 1

    elif n == 110:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/genre.nhn?genre=110&page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_mof'})
            title = f_container.find('li').find('a').attrs['title']
            if pre_title==title:
                print(n)
                n = n + 1
                break
            pre_title=title
            con = f_container.findAll('li')

            for li in con:
                title_list.append([])
                f_title = li.find('a').attrs['title']
                f_url = li.find('a').attrs['href']
                title_list[total].append(f_title)
                title_list[total].append("https://m.novel.naver.com/"+f_url)
                title_list[total].append('네이버 웹소설')
                print(f_title)
                print(f_url)
                total = total + 1

            i = i+1

    elif n == 111:
        i = 1
        sam_url = "https://novel.naver.com/webnovel/finish.nhn?page={}"
        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(sam_url)
        soup2 = bs4.BeautifulSoup(driver.page_source, "html.parser")

        time.sleep(3)
        comm = driver.find_element_by_css_selector("#wrap > div.ly_event_contest > div.contest_cont > a.lk_close")
        comm.click()
        time.sleep(2)
        while True:
            url = sam_url.format(i)
            req = requests.get(url)
            source = req.content
            bs_obj = BeautifulSoup(source, "html.parser")

            if 'list_type1 v2 NE=a:lst_end' in bs_obj:
                f_container = bs_obj.find('ul', {'class', 'list_type1 v2 NE=a:lst_end'})
                title = f_container.find('li').find('a').attrs['title']
                if pre_title == title:
                    print(n)
                    n = n + 1
                    break
                pre_title = title
                con = f_container.findAll('li')

                for li in con:
                    title_list.append([])
                    f_title = li.find('a').attrs['title']
                    f_url = li.find('a').attrs['href']
                    title_list[total].append(f_title)
                    title_list[total].append("https://m.novel.naver.com/" + f_url)
                    title_list[total].append('네이버 웹소설')
                    print(f_title)
                    print(f_url)
                    total = total + 1

                i = i + 1
            else:
                n = n + 1
                break

    #n = n + 1

    if n == 112:
        Flag = False
        break

data = pd.DataFrame(title_list, columns=['작품명', '링크', '연재 플랫폼'])
data.to_csv('naver_webnovel.csv', encoding='utf-8-sig', index=False)

print("저장 완료.\n")