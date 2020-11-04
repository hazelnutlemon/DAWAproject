import pymysql
from app import main_dbconn

def get_top():
    conn = main_dbconn.get_connection()

    sql = '''
        select novel.idnovel, novel.title, novel.genre, review.score, novel.img_src from novel left outer join review on novel.idnovel=review.novel where (review.term="2020-10-01") order by review.score desc limit 10;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_main = {
            'idnovel' : obj[0],
            'title' : obj[1],
            'genre' : obj[2],
            'score' : obj[3],
            'pic' : obj[4]

        }
        data_list.append(data_main)

    conn.close

    return data_list
