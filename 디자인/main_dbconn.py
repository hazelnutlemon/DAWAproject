import pymysql

def get_connection():
    conn = pymysql.connect(host='localhost',
                                  user='root',
                                  password='dlsvlslxm00!',
                                  db='webnoveldb',
                                  charset='utf8')
    return conn