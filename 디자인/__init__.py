

from flask import Flask, render_template
from app import mod_dbconn
from app import get_main
from app import get_list
import pymysql
from app import main_dbconn
from flask import Flask, request, session, render_template, url_for
import sqlite3
import math

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

    cursor.execute("select title, img_src, genre, age, idnovel from novel order by idnovel asc where idnovel = %s order by idnovel desc",(3,))
    row = cursor.fetchall()

    data_list2 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'idnovel': obj[4]

        }
        data_list2.append(list_data)

    conn.close

    return data_list2

def selecte_page(list_limit, page):

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    offset = (page-1) * list_limit
    sql = "select title, img_src, genre, age, idnovel from novel order by idnovel asc limit %s offset %s"

    cursor.execute(sql, (list_limit, offset))
    row = cursor.fetchall()

    data_list2 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[1],
            'genre' : obj[2],
            'age' : obj[3],
            'idnovel': obj[4]
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

    cursor.execute("SELECT novel.title, novel.age, novel.genre, novel.publisher, novel.total, novel.intro, novel.img_src, novel.idnovel, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5 \
                FROM novel, textrank where novel.idnovel = textrank.novel = %s order by idnovel desc",(3,))
    row = cursor.fetchall()

    data_list3 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[6],
            'genre' : obj[2],
            'age' : obj[1],
            'publisher' : obj[3],
            'total' : obj[4],
            'intro' : obj[5],
            'idnovel': obj[7],
            'word1': obj[8],
            'word2': obj[9],
            'word3': obj[10],
            'word4': obj[11],
            'word5': obj[12],
        }
        data_list3.append(list_data)

    conn.close

    return data_list3

def selectep_page(list_limit, page):

    conn = main_dbconn.get_connection()
    cursor = conn.cursor()

    offset = (page-1) * list_limit
    sql = "SELECT novel.title, novel.age, novel.genre, novel.publisher, novel.total, novel.intro, novel.img_src, novel.idnovel, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5 \
                FROM novel, textrank where novel.idnovel = textrank.novel order by idnovel asc limit %s offset %s"

    cursor.execute(sql, (list_limit, offset))
    row = cursor.fetchall()

    data_list3 = []

    for obj in row :
        list_data = {
            'title' : obj[0],
            'img_src' : obj[6],
            'genre' : obj[2],
            'age' : obj[1],
            'publisher' : obj[3],
            'total' : obj[4],
            'intro' : obj[5],
            'idnovel': obj[7],
            'word1': obj[8],
            'word2': obj[9],
            'word3': obj[10],
            'word4': obj[11],
            'word5': obj[12],
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

def get_context_data(self, **kwargs):
    context = super(PostLV, self).get_context_data(**kwargs)
    paginator = context['paginator']
    page_numbers_range = 10
    max_index = len(paginator.page_range)

    page = self.request.GET.get('page')
    current_page = int(page) if page else 1

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    context['page_range'] = page_range
    return context

if __name__=='__main__':
    app.run(debug=True)

from app import app
