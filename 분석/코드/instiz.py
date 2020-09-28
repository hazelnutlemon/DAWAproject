import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse

tmp = input("작품제목 : ")
n = 1
total = 0
base_url = "https://www.instiz.net/popup_search.htm#gsc.tab=0&gsc.q=" + parse.quote(tmp) + "&gsc.page={}"
Flag = True
while True:
    # 작품의 링크
    url = base_url.format(n)
    driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    print("Page = " + str(n))
    bs_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")

    base_xpath = '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div[2]/div/div[1]/div[{}]/div[1]/div[2]/div[2]'

    for i in range(10):
        xpath = base_xpath.format(i + 1)
        try:
            box_area = driver.find_element_by_xpath(xpath)
        except:
            Flag = False
            break

        baurl = box_area.text

        test = 'https://'
        test2 = 'www.'

        if test in baurl:
            req = requests.get(baurl)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")

            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')
            comm = soup.find('div', {'class', 'comment_line'})

            if "인스티즈(instiz)" in content:
                continue
            else:
                date = soup.find("span", itemprop='datePublished')
                date = date.get("content")[0:10]

            total = total + 1
            print("title")
            print(title)
            con = content.split("-")[1]
            print("date")
            print(date)
            print("content")
            print(con)
            if comm == None:
                continue
            else:
                print("comment")

                comment = soup.findAll('div',{'class','comment_line'})
                for review in comment:
                    print(review.text)


        elif test2 in baurl:
            m_url = "https://" + baurl
            req = requests.get(m_url)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")

            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')
            comm = soup.find('div', {'class', 'comment_line'})


            if "인스티즈(instiz)" in content:
                continue
            else:
                date = soup.find("span", itemprop='datePublished')
                date = date.get("content")[0:10]

            total = total + 1
            print("title")
            print(title)
            con = content.split("-")[1]
            print("date")
            print(date)
            print("content")
            print(con)
            if comm == None:
                continue
            else:
                print("comment")

                comment = soup.findAll('div',{'class','comment_line'})
                for review in comment:
                    print(review.text)

        else:
            mm_url = "https://www." + baurl
            # print(mm_url)
            req = requests.get(mm_url)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")

            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')
            comm = soup.find('div', {'class', 'comment_line'})

            if "인스티즈(instiz)" in content:
                continue
            else:
                date = soup.find("span", itemprop='datePublished')
                date = date.get("content")[0:10]

            total = total + 1
            print("title")
            print(title)
            con = content.split("-")[1]
            print("date")
            print(date)
            print("content")
            print(con)
            if comm == None:
                continue
            else:
                print("comment")

                comment = soup.findAll('div',{'class','comment_line'})
                for review in comment:
                    print(review.text)


    if (Flag == False):
        print("총 게시글 수")
        print(total)
        print("프로그램을 종료합니다")
        break
    n = n + 1