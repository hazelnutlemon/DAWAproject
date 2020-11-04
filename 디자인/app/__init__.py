

from flask import Flask, render_template
from app import mod_dbconn
from app import get_main
from app import get_list
from app import get_gerne
import pymysql
from app import main_dbconn
from app import gerne_dbconn
from flask import Flask, request, session, render_template, url_for
import sqlite3
import math
from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


# 여기부터 추가
@app.route('/db')
def select():
    db_class = mod_dbconn.Database()

    sql2 = "SELECT title, age, genre, publisher, total, intro, img_src, idnovel \
                FROM webnoveldb.novel"
    row2 = db_class.executeAll(sql2)
    print(row2)

    return render_template('db.html', resultData=row2[0])


# 여기까지 추가

@app.route('/main')
def index():

    content_list=get_main.get_top()

    html = render_template('index.html', data_list=content_list)
    return html

@app.route('/gerne')
def gerne():

    content_list=get_gerne.get_gerner()

    html = render_template('gerne.html', data_list=content_list)
    return html

@app.route('/menu')
def menu():

    return render_template('menu.html')

@app.route('/mist/')
def mist():

    total_list=get_list.get_list()

    return render_template('list.html', data_list2=total_list)

def selecte():

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT novel.title, novel.img_src, novel.genre, novel.age, author.name, novel.idnovel from novel INNER JOIN author ON novel.idnovel = author.novel \
                   order by novel.idnovel asc where novel.idnovel = %s order by novel.idnovel desc",(3,))
    row = cursor.fetchall()

    data_list2 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'author' : obj[4],
            'idnovel' : obj[5]

        }
        data_list2.append(list_data)

    conn.close

    return data_list2

def selecte_page(list_limit, page):

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    offset = (page-1) * list_limit
    sql = "SELECT novel.title, novel.img_src, novel.genre, novel.age, author.name, novel.idnovel from novel INNER JOIN author ON novel.idnovel = author.novel order by idnovel asc limit %s offset %s"

    cursor.execute(sql, (list_limit, offset))
    row = cursor.fetchall()

    data_list2 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'author' : obj[4],
            'idnovel' : obj[5]
        }
        data_list2.append(list_data)

    conn.close

    return data_list2

def select_count():

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("select count(idnovel) from novel")
    data_list2 = cursor.fetchone()
    conn.close()
    return data_list2[0]

def list_test():
    list = selecte()
    print(list)

@app.route('/lists')
def lists():
    lists = selecte()
    return render_template('lists2.html', lists=lists)

@app.route('/list/<int:page>')
def list(page):
    list_num = 20
    lists_count = select_count()
    page_count = int(lists_count/list_num)

    lists = selecte_page(list_num, page)

    return render_template('list2.html', lists=lists, page_count=page_count)

def selectp():

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT novel.*, author.name, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5, \
                    aspect_character.reaction1, aspect_character.reaction2, aspect_character.reaction3, aspect_character.reaction4, aspect_character.reaction5, \
                    aspect_mood.reaction1, aspect_mood.reaction2, aspect_mood.reaction3, aspect_mood.reaction4, aspect_mood.reaction5, aspect_story.reaction1, aspect_story.reaction2, aspect_story.reaction3, aspect_story.reaction4, aspect_story.reaction5  \
                    FROM novel \
                    INNER JOIN textrank ON novel.idnovel = textrank.novel \
                    INNER JOIN author ON textrank.novel = author.novel \
                    INNER JOIN aspect_character ON author.novel = aspect_character.novel \
                    INNER JOIN aspect_mood ON aspect_character.novel = aspect_mood.novel \
                    INNER JOIN aspect_story ON aspect_mood.novel = aspect_story.novel = %s order by idnovel desc", (3,))

    row = cursor.fetchall()

    data_list3 = []

    for obj in row :
        list_data = {
            'title' : obj[1],
            'age' : obj[2],
            'genre' : obj[3],
            'publisher' : obj[4],
            'pub_date' : obj[5],
            'total' : obj[6],
            'complete' : obj[7],
            'intro': obj[8],
            'img_src': obj[9],
            'joara' : obj[10],
            'munpia' : obj[11],
            'kakaopage' : obj[12],
            'ridibooks' : obj[13],
            'serieson' : obj[14],
            'naverwebnovel': obj[15],
            'author': obj[16],
            'word1': obj[17],
            'word2': obj[18],
            'word3': obj[19],
            'word4': obj[20],
            'word5': obj[21],
            'c_reaction1': obj[22],
            'c_reaction2': obj[23],
            'c_reaction3': obj[24],
            'c_reaction4': obj[25],
            'c_reaction5': obj[26],
            'm_reaction1': obj[27],
            'm_reaction2': obj[28],
            'm_reaction3': obj[29],
            'm_reaction4': obj[30],
            'm_reaction5': obj[31],
            's_reaction1': obj[32],
            's_reaction2': obj[33],
            's_reaction3': obj[34],
            's_reaction4': obj[35],
            's_reaction5': obj[36]

        }
        data_list3.append(list_data)

    conn.close

    return data_list3

def selectep_page(list_limit, page):

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    offset = (page-1) * list_limit
    sql = "SELECT novel.*, author.name, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5, \
                    aspect_character.reaction1, aspect_character.reaction2, aspect_character.reaction3, aspect_character.reaction4, aspect_character.reaction5, \
                    aspect_mood.reaction1, aspect_mood.reaction2, aspect_mood.reaction3, aspect_mood.reaction4, aspect_mood.reaction5, aspect_story.reaction1, aspect_story.reaction2, aspect_story.reaction3, aspect_story.reaction4, aspect_story.reaction5  \
                    FROM novel \
                    INNER JOIN textrank ON novel.idnovel = textrank.novel \
                    INNER JOIN author ON textrank.novel = author.novel \
                    INNER JOIN aspect_character ON author.novel = aspect_character.novel \
                    INNER JOIN aspect_mood ON aspect_character.novel = aspect_mood.novel \
                    INNER JOIN aspect_story ON aspect_mood.novel = aspect_story.novel \
            order by idnovel asc limit %s offset %s"

    cursor.execute(sql, (list_limit, offset))
    row = cursor.fetchall()

    data_list3 = []

    for obj in row :
        list_data = {
            'title' : obj[1],
            'age' : obj[2],
            'genre' : obj[3],
            'publisher' : obj[4],
            'pub_date' : obj[5],
            'total' : obj[6],
            'complete' : obj[7],
            'intro': obj[8],
            'img_src': obj[9],
            'joara' : obj[10],
            'munpia' : obj[11],
            'kakaopage' : obj[12],
            'ridibooks' : obj[13],
            'serieson' : obj[14],
            'naverwebnovel': obj[15],
            'author': obj[16],
            'word1': obj[17],
            'word2': obj[18],
            'word3': obj[19],
            'word4': obj[20],
            'word5': obj[21],
            'c_reaction1': obj[22],
            'c_reaction2': obj[23],
            'c_reaction3': obj[24],
            'c_reaction4': obj[25],
            'c_reaction5': obj[26],
            'm_reaction1': obj[27],
            'm_reaction2': obj[28],
            'm_reaction3': obj[29],
            'm_reaction4': obj[30],
            'm_reaction5': obj[31],
            's_reaction1': obj[32],
            's_reaction2': obj[33],
            's_reaction3': obj[34],
            's_reaction4': obj[35],
            's_reaction5': obj[36]

        }
        data_list3.append(list_data)

    conn.close

    return data_list3


def selectp_count():
    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("select count(idnovel) from novel")
    data_list3 = cursor.fetchone()
    conn.close()
    return data_list3[0]


def listp_test():
    listp = selectp()
    print(listp)


@app.route('/content')
def listsp():
    listsp = selectsp()
    return render_template('lists2.html', lists=listsp)


@app.route('/content/<int:idnovel>')
def listp(idnovel):
    listp_num = 1
    listsp_count = selectp_count()
    pagep_count = int(listsp_count / listp_num)

    listsp = selectep_page(listp_num, idnovel)

    return render_template('content.html', lists=listsp, page_count=pagep_count)

def selecter():

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT novel.title, novel.img_src, novel.genre, novel.age, author.name, novel.idnovel from novel INNER JOIN author ON novel.idnovel = author.novel \
                    where ridibooks is not NULL order by idnovel desc")
    row = cursor.fetchall()

    data_listr = []

    for obj in row :
        list_datar = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'author' : obj[4],
            'idnovel': obj[5]

        }
        data_listr.append(list_datar)

    conn.close

    return data_listr

def selecter_page(list_limit, page):

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    offset = (page-1) * list_limit
    sql = "SELECT novel.title, novel.img_src, novel.genre, novel.age, author.name, novel.idnovel from novel INNER JOIN author ON novel.idnovel = author.novel \
           where ridibooks is not NULL order by idnovel asc limit %s offset %s"

    cursor.execute(sql, (list_limit, offset))
    row = cursor.fetchall()

    data_listr = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'author' : obj[4],
            'idnovel' : obj[5]
        }
        data_listr.append(list_data)

    conn.close

    return data_listr

def selectr_count():

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    cursor.execute("select count(ridibooks) from novel where ridibooks is not NULL")
    data_listr = cursor.fetchone()
    conn.close()
    return data_listr[0]

def listr_test():
    listr = selecter()
    print(listr)

@app.route('/ridibooks')
def listsr():
    listsr = selecter()
    return render_template('ridibooks.html', lists=listsr)

@app.route('/ridibooks/<int:page>')
def ridibooks(page):
    list_num = 20
    listsr_count = selectr_count()
    pager_count = int(listsr_count/list_num)

    listsr = selecter_page(list_num, page)

    return render_template('ridibooks.html', lists=listsr, page_count=pager_count)

@app.route("/main", methods=['GET', 'POST'])
def post():
    if(request.method =='GET'):
        searchcontent = request.args.get('searchcontent')
        print(searchcontent)
        contentList = get_list.get_contentList(searchcontent, '')
        return render_template('search.html', contentList=contentList)

    elif(request.method == 'POST'):
        searchcontent = request.form['input']
        print(searchcontent)
        contentList = get_list.get_contentList(searchcontent, '')
        return render_template('search.html', contentList=contentList)


if __name__=='__main__':
    app.run(debug=True)

