import pymysql

def get_connection():
    conn = pymysql.connect(host='localhost',
                                  user='root',
                                  password='',
                                  db='webnoveldb',
                                  charset='utf8')
    return conn