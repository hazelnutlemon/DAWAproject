import pymysql
from app import gerne_dbconn

def get_gerner():
    conn = gerne_dbconn.get_connection()

    sql = '''
        select a.idnovel, a.title, a.genre, b.name, a.img_src from (select * from novel n left outer join review c on n.idnovel=c.novel 
        where (c.term="2020-10-01") order by c.score) a left outer join author b on a.idnovel=b.novel where a.genre like "%로맨스%" order by a.score desc;
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_gerne = {
            'idnovel' : obj[0],
            'title' : obj[1],
            'genre' : obj[2],
            'score' : obj[3],
            'pic' : obj[4]

        }
        data_list.append(data_gerne)

    conn.close

    return data_list
