import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse

tmp=input("작품제목 : ")


n = 1
total = 1
pre_tit = None
n_url = "https://search.dcinside.com/post/p/{}/sort/latest/q/" + parse.quote(tmp)
Flag = True
while True:
    m_url = n_url.format(n)
    req = requests.get(m_url)
    source = req.content

    bs_obj = BeautifulSoup(source, "html.parser")

    f_container = bs_obj.find('ul', {'class', 'sch_result_list'})

    tit = f_container.find('a', {'class', 'tit_txt'})
    #print(tit)

    if pre_tit == tit:
        break
    pre_tit == tit

    con = f_container.findAll('li')

    for li in con:
        n_url = li.find('a').attrs['href']

        driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
        driver.get(n_url)
        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

        if "성인인증" in soup.find('h2').text:
            continue

        else:
            title = soup.head.find("meta", {"name": "title"}).get('content').split("-")[0]
            date = soup.find('span', class_='gall_date')
            date = date.get("title")[0:10]
            content= driver.find_element_by_xpath('// *[ @ id = "container"] / section / article[2] / div[1] / div / div[1] / div[1]').text
            print("title")
            print(title)
            print("date")
            print(date)
            print("content")
            print(content)

            cmm_n = soup.find('div', {'class', 'comment_count'})
            num = cmm_n.find('span').text
            #print(num)
            #num = int(cmm_n)
            if num == "0":
                continue
            else:
                print("comment")
                comment = soup.find('div', {'class', 'comment_box'})
                com_2 = comment.findAll('p')
                for review in com_2:
                    print(review.text)

        total = total + 1
        sto = str(total)
        print("게시글 수: " + sto)

    n = n+1
    sto = str(total)
    print("게시글 수: "+sto)


driver.close()

