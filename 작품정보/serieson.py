import requests
from bs4 import BeautifulSoup

req = requests.get('https://series.naver.com/novel/detail.nhn?productNo=3200031')
source = req.text
soup = BeautifulSoup(source, 'html.parser')

################## 제목, 화수 ####################
f_container = soup.find('div', {'class', 'end_head'})
container = f_container.find('h2')
con = container.text.split("[")[0]
con2 = con.split("-")[0]
print("제목: " + con2)
count = container.find('em')
count1 = count.text.replace("- 총","")
count2 = count1.replace("화/","")
if '미완결' in count2:
    count3 = count2.replace("미완결","")
else:
    count3 = count2.replace("완결","")
print("화수: " + count3)

################## 저자 ####################
box = soup.find(id='container')
info_list = box.find('li', {'class', 'info_lst'})
li = info_list.findAll('li')
print("저자: " + li[0].find('a').text)

############# 그림 유무 판단, 출력 ##############
if "그림" in li[1].find('span'):
    n = 1
else:
    n = 0
if n == 1:
    print("그림: " + li[1].find('a').text)

############# 장르, 출판사, 등급 ###############
print("장르: " + li[1+n].find('a').text)
print("출판사: " + li[2+n].find('a').text)
print("등급: " + li[3+n].text.replace("등급 ",""))

############# 완결 여부에 따른 프린트 ###############
update = li[4+n].text.replace("업데이트 ","")
if n == 1:
    print("최근 업데이트:", update.replace("(완결)",""))
else:
    print("최근 업데이트:", update.replace("(미완결)", ""))
if n == 1:
    print("완결여부: 완결")
else:
    print("완결여부: 미완결")

############### 별점 #################
f_scorearea = soup.find('div', {'class', 'score_area'})
ff_scorearea = f_scorearea.find('em')
scorearea = ff_scorearea.text
print("별점: " + scorearea)

############### 소개 #################
f_dsc = soup.find('div', {'class', '_synopsis'})
print("소개: " + f_dsc.text)



################## 검색 ####################
search = "https://series.naver.com/search/search.nhn?t=all&fs=novel&q="
search_for = input("검색: ")
print("\n---------------------\n")
web_search = search + search_for.replace(" ", "+")

req = requests.get(web_search)
source = req.text
soup = BeautifulSoup(source, 'html.parser')

link = soup.find('ul', {'class', 'lst_list'})
href = link.find('a').attrs['href']

novel_url = "https://series.naver.com/" + href

req = requests.get(novel_url)
source = req.text
soup = BeautifulSoup(source, 'html.parser')

################## 제목, 화수 ####################
f_container = soup.find('div', {'class', 'end_head'})
container = f_container.find('h2')
con = container.text.split("[")[0]
con2 = con.split("-")[0]
print("제목: " + con2)
count = container.find('em')
count1 = count.text.replace("- 총","")
count2 = count1.replace("화/","")
if '미완결' in count2:
    count3 = count2.replace("미완결","")
else:
    count3 = count2.replace("완결","")
print("화수: " + count3)

################## 저자 ####################
box = soup.find(id='container')
info_list = box.find('li', {'class', 'info_lst'})
li = info_list.findAll('li')
print("저자: " + li[0].find('a').text)

############# 그림 유무 판단, 출력 ##############
if "그림" in li[1].find('span'):
    n = 1
else:
    n = 0
if n == 1:
    print("그림: " + li[1].find('a').text)

############# 장르, 출판사, 등급 ###############
print("장르: " + li[1+n].find('a').text)
print("출판사: " + li[2+n].find('a').text)
print("등급: " + li[3+n].text.replace("등급 ",""))

############# 완결 여부에 따른 프린트 ###############
update = li[4+n].text.replace("업데이트 ","")

if '미완결' in count2:
    a = 0
else:
    a = 1

if a == 1:
    print("최근 업데이트:", update.replace("(완결)",""))
else:
    print("최근 업데이트:", update.replace("(미완결)", ""))
if a == 1:
    print("완결여부: 완결")
else:
    print("완결여부: 미완결")

############### 별점 #################
f_scorearea = soup.find('div', {'class', 'score_area'})
ff_scorearea = f_scorearea.find('em')
scorearea = ff_scorearea.text
print("별점: " + scorearea)

############### 소개 #################
f_dsc = soup.find('div', {'class', '_synopsis'})
print("소개: " + f_dsc.text)