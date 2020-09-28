#!/usr/bin/env python
# coding: utf-8

# # 네이버 웹소설

import requests
from bs4 import BeautifulSoup

req = requests.get('https://novel.naver.com/webnovel/list.nhn?novelId=699567')
source = req.content
soup = BeautifulSoup(source, 'html.parser')

################## 제목 ####################
container = soup.find('h2')
con = container.text
print("제목: " + con)

################## 글, 그림 ####################
f_wri_ill = soup.find('p', {'class', 'writer'})
author = f_wri_ill.find('a', {'class', 'NPI=a:writer'})
aut = author.text
illustrator = f_wri_ill.find('a', {'class', 'NPI=a:illustrator'})
ill = illustrator.text
print("글: " + aut)
print("그림: " + ill)

################## 별점 ####################
f_stargrade = soup.find('p', {'class', 'grade_area'})
ff_stargrade = f_stargrade.find('em')
stargrade = ff_stargrade.text
print("별점: " + stargrade)

############### 관심, 연재일, 장르 ##################
info = soup.find('p', {'class', 'info_book'})
f_like = info.find('span', {'id': 'concernCount'})
like = f_like.text

f_publish = info.find('span', {'class', 'publish'})
publish = f_publish.text.replace("연재","")

f_genre = info.find('span', {'class', 'genre'})
genre = f_genre.text

print("관심: " + like)
print("연재일: " + publish)
print("장르: " + genre)

################## 연재 화수 ####################
list_count = soup.find('span', {'class', 'total'})
count1 = list_count.text.replace("(","")
count = count1.replace(")", "")
print("연재 화수: " + count)

################## 소개 ####################
f_dsc = soup.find('p', {'class', 'dsc'})
dsc = f_dsc.text
print("소개: " + dsc)