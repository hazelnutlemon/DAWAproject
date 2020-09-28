#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup

BASE_URL = "https://gall.dcinside.com/mgallery/board/lists?id=genrenovel"

params = {
            'id': 'genrenovel',}

headers = {
    'User-Agent' : "Mozilla/5.0 (Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

resp = requests.get(BASE_URL, params=params, headers=headers)

soup = BeautifulSoup(resp.content, 'html.parser')

contents = soup.find('tbody').findAll('tr')

for i in contents:
    print('-' * 15)

    title_tag = i.find('a')
    title = title_tag.text
    print("제목: ", title)

    writer_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='nickname')
    if writer_tag is not None:
        writer = writer_tag.text
        print("글쓴이: ", writer)

    else:
        print("글쓴이: ", "없음")

    ip_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='ip')
    if ip_tag is not None:
        ip = ip_tag.text
        print("ip: ", ip)

    date_tag = i.find('td', class_='gall_date')
    date_dict = date_tag.attrs

    if len(date_dict) == 2:
        print("날짜: ", date_dict['title'])

    else:
        print("날짜: ", date_tag.text)
        pass

    views_tag = i.find('td', class_='gall_count')
    views = views_tag.text
    print("조회수: ", views)

    recommend_tag = i.find('td', class_='gall_recommend')
    recommend = recommend_tag.text
    print("추천수: ", recommend)

    link = i.find('td', class_='gall_tit ub-word')
    href = link.find('a').attrs['href']
    if href=="javascript:;":
        continue
    content_url = "https://gall.dcinside.com/" + href

    print(content_url)

    req = session.get(content_url,headers=header)
    source = req.content
    html = BeautifulSoup(source, 'html.parser')

    body=html.find('div',{'class','view_content_wrap'})
    title=body.find('h3',{'class','title ub-word'})
    print(title.text)
    context=body.find('div',{'class','writing_view_box'})
    print(context.text)


# In[ ]:




