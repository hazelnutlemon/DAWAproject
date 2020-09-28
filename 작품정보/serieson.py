
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import time

def hasxpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


driver = webdriver.Chrome('/Users/home/chromedriver_mac64_2/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
id = "ys913x"
pw = "dlsvlslxm00"
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(0.5) ## 0.5초



n=1000
base_url= "https://series.naver.com/novel/categoryProductList.nhn?categoryTypeCode=all&page={}"
driver.get(base_url)
driver.implicitly_wait(3)
Flag = True

title_list = []
total = 0
pre_title = None

while True:
    url = base_url.format(n)
    req = requests.get(url)
    source = req.content

    bs_obj = BeautifulSoup(source, "html.parser")

    f_container = bs_obj.find('div', {'class', 'lst_thum_wrap'})

    title = f_container.find('h3').find('a').attrs['title']

    if pre_title == title:
        break
    pre_title = title
    con = f_container.findAll('h3')


    for h3 in con:


        title_list.append([])
        f_title = h3.find('a').attrs['title']
        n_url = h3.find('a').attrs['href']

        m_url = "https://series.naver.com/" + n_url

        #em = h3.find('em', {'class', 'ico_age n19'})
        #print(em)
        #if em in h3:
        #    continue
        #else:
            #driver.implicitly_wait(3)
            #driver.get(m_url)

        driver.implicitly_wait(3)
        driver.get(m_url)

        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
        #more = soup.find('a', {'class', 'lk_more _toggleMore(synopsis) NPI=a:more'})

        box = soup.find(id='container')
        info_list = box.find('li', {'class', 'info_lst'})
        li = info_list.find_all('li')
        #print(li)

        author = li[2].find('a').text

        f_img = soup.find('a', {'class', 'pic_area'})
        if f_img == None:
            f_img = soup.find('span', {'class', 'pic_area'})
        temp_img = f_img.find('img')
        img_scr = temp_img.get('src')

        if "그림" in li[1].find('span'):
            ba = 1
        else:
            ba = 0

        genre = li[1].find('a').text
        publisher = li[3 + ba].find('a').text
        age = li[4 + ba].text.replace("등급 ", "")

        complete = li[0].text

        if "최신순" in driver.find_element_by_xpath('// *[ @ id = "content"] / table / thead / tr / th[1] / div / button').text:
            driver.find_element_by_xpath('//*[@id="content"]/table/thead/tr/th[1]/div/button').click()
        pub_date = driver.find_element_by_xpath('//*[@id="volumeList"]/tr[1]/td[1]/div/em').text
        print(pub_date)

        find_total = soup.find('h5', {'class', 'end_total_episode'})
        m_total = find_total.find('strong').text
        print(m_total)

        if "더보기" in driver.find_element_by_xpath('//*[@id="content"]/div[2]/div').text:
            if hasxpath('//*[@id="content"]/div[2]/div[1]/span/a') == True:
                driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/span/a').click()
                intro = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]')
            elif hasxpath('// *[ @ id = "content"] / div[2] / div[1] / b.. / span / a') == True:
                driver.find_element_by_xpath('// *[ @ id = "content"] / div[2] / div[1] / b.. / span / a').click()
                intro = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]')
            elif hasxpath('// *[ @ id = "content"] / div[2] / div[1] / br.. / span / a') == True:
                driver.find_element_by_xpath('// *[ @ id = "content"] / div[2] / div[1] / br.. / span / a').click()
                intro = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]')
            else:
                break

            m_intro = intro.text.replace("접기", "")
        else:
            m_intro = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div').text

        print(f_title)
        print(m_intro)

        title_list[total].append(f_title)
        title_list[total].append(author)
        title_list[total].append(genre)
        title_list[total].append(img_scr)
        title_list[total].append(pub_date)
        title_list[total].append(complete)
        title_list[total].append(m_intro)
        title_list[total].append(publisher)
        title_list[total].append(age)
        title_list[total].append(m_total)
        title_list[total].append("https://m.series.naver.com"+n_url)


        total = total + 1




    n = 2

data = pd.DataFrame(title_list, columns = ['title', 'author', 'genre', 'img_scr', 'pub_date', 'complete', 'intro', 'publisher', 'age', 'total', 'series'])
data.to_csv('naver_serieson.csv', encoding='utf-8-sig', index=False)

driver.close()

print("저장 완료.\n")

