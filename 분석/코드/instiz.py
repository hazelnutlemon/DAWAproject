import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib import parse

def hasxpath(xapth):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


url = "https://www.instiz.net/m/index.htm?welcome=1"
driver = webdriver.Chrome('C:/Users/luvub/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)
try:
    driver.find_element_by_xpath('/html/body/div[8]/div/div[4]').click()
except:
    pass

tmp=input("작품제목 : ")
n=1
base_url= "https://www.instiz.net/popup_search.htm#gsc.tab=0&gsc.q=" + parse.quote(tmp) + "&gsc.page={}"
Flag=True
while True:
    #작품의 링크
    url=base_url.format(n)
    driver.implicitly_wait(5)
    driver.get(url)
    print("Page = " + str(n))
    bs_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")


    base_xpath='//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div[2]/div/div[1]/div[{}]/div[1]/div[2]/div[2]'

    for i in range(10):
        xpath=base_xpath.format(i+1)
        try:
            box_area=driver.find_element_by_xpath(xpath)
        except:
            Flag=False
            break

        baurl = box_area.text

        test = 'https://'
        test2 = 'www.'

        if test in baurl:
            #print(baurl)
            driver.get(baurl)
            req = requests.get(baurl)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")
            #print(soup)
            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')

            if "대한민국 최대의 연예·오락 커뮤니티" in content:
                continue

            date = soup.head.find("meta", {"name": "description"}).get('content')
            date = date[0:13]
            count = soup.find('a', {'class', 'cmt'})
            con2 = soup.find('div', {'class', 'memo_content'})
            for tag in con2.find_all(['span']):
                tag.replace_with('')
            print(title, date)
            print(count.text)
            print(con2)

            try:
                temp = driver.find_element_by_xpath('//*[@id="ajax_table"]/tbody/tr[1]/td[2]/div[2]').text.replace(
                    '•••답글', '')
                print(temp)
            except:
                pass



        elif test2 in baurl:
            m_url = "https://" + baurl
            driver.get(m_url)
            req = requests.get(m_url)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")

            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')

            if "대한민국 최대의 연예·오락 커뮤니티" in content:
                continue

            date = soup.head.find("meta", {"name": "description"}).get('content')
            date = date[0:13]
            count = soup.find('a', {'class', 'cmt'})
            con2 = soup.find('div', {'class', 'memo_content'})
            for tag in con2.find_all(['span']):
                tag.replace_with('')
            print(title, date)
            print(count.text)
            print(con2)

            try:
                temp = driver.find_element_by_xpath('//*[@id="ajax_table"]/tbody/tr[1]/td[2]/div[2]').text.replace(
                    '•••답글', '')
                print(temp)
            except:
                pass



        else:
            mm_url = "https://www." + baurl
            driver.get(mm_url)
            req = requests.get(mm_url)
            source = req.content

            soup = BeautifulSoup(source, "html.parser")
            print(soup)
            title = soup.head.find("meta", {"property": "og:title"}).get('content')
            content = soup.head.find("meta", {"name": "description"}).get('content')

            if "대한민국 최대의 연예·오락 커뮤니티" in content:
                continue

            date = soup.head.find("meta", {"name": "description"}).get('content')
            date = date[0:13]
            count = soup.find('a', {'class', 'cmt'})
            con2 = soup.find('div', {'class', 'memo_content'})
            for tag in con2.find_all(['span']):
                tag.replace_with('')
            print(title, date)
            print(count.text)
            print(con2)

            try:
                temp = driver.find_element_by_xpath('//*[@id="ajax_table"]/tbody/tr[1]/td[2]/div[2]').text.replace(
                    '•••답글', '')
                print(temp)
            except:
                pass

    if(Flag==False):
        print("프로그램을 종료합니다")
        break
    n=n+1