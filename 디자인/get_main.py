import pymysql
from app import main_dbconn

def get_top():
    conn = main_dbconn.get_connection()

    sql = '''
        select title, pic, link
        from topmain
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_main = {
            'title' : obj[0],
            'pic' : obj[1],
            'link' : obj[2]
        }
        data_list.append(data_main)

    conn.close

    return data_list