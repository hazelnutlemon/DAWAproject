import re

def make_date_list():
    date_array = [['2020-01-01', 0, 0], ['2020-02-01', 0, 0], ['2020-03-01', 0, 0], ['2020-04-01', 0, 0],
                  ['2020-05-01', 0, 0], ['2020-06-01', 0, 0],
                  ['2020-07-01', 0, 0], ['2020-08-01', 0, 0], ['2020-09-01', 0, 0], ['2020-10-01', 0, 0]
                  ]

    # date 형식이 2020-07-01일수도 2020.07.01일 수도 있지.
    # 배열 위치는 2020-07-01을 int(re.compile)을 이용해 숫자만 남긴다.
    # 202007/01

    return date_array

def date_list_pos(date):
    num = re.compile('[^ 0-9]+')
    date = num.sub('', date).replace('  ', ' ')  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    month = int(date[4:6])
    pos = (month - 1)

    return pos