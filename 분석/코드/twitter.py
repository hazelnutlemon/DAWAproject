# 코드 제작자 및 모듈화 : 한승주 2015722084

import twint
import re
import nest_asyncio

# 특수 문자 제거 : 숫자, 영어, 한글을 제외 모든 글자 지우기
def clean_name(term):
    print("검색 키워드 제거")
    cleaned = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', '', term) # 특수문자 제거
    return cleaned

# 안씀
def tweet_clean(tweet_text):
    # URL 제거 시도했으나 경우의 수가 많아 패스. 분석에서 연관성 확인 과정에서 안나오지 않을까
    pattern = 'pic.twitter.com/[a-zA-Z0-9]+'
    tweet_text = re.sub(pattern=pattern, repl='',string=tweet_text) # pic.twitter.com/XXXXXXX 사진 링크 삭제
    return tweet_text

def tweet_scraping(search):
    nest_asyncio.apply() # Runtime Error 발생하는 경우를 대비 - 코드 휴식을 위한 추가 코드
    
    #tweets = []
    
    # 검색 시작 : 2019-01-01 / 끝 : 2020-09-30
    #since = "2019-01-01"
    #until = "2020-09-30"
    #print("검색 기간 설정")
    
    # Twint를 이용한 트위터 검색 결과
    c = twint.Config()
    print("config 만들어줌")
    
    # 파라미터 설정
    c.Search = search
    #c.Since = since
    #c.Until = until
    c.Popular_tweets = True
    c.Store_object = True
    #c.Hide_output = True
    print("파라미터 설정함")
    
    print("수집 시작함")
    tweets = twint.run.Search(c) # 트윗 수집 시작
    tweet_data = [] # 수집한 트위터를 list 타입으로 저장
    
    print("필요한 부분 추출")
    for tweet in tweets:
        date = tweet['date'] # YYYY-MM-DD 형식으로 작성 날짜 저장
        tweet_text = tweet['tweet'] # 트윗 내용 저장
        tweet_data.append([date,tweet_text])
        
    #total = len(tweets) # 수집한 트윗 개수는 따로
    #print("2019-01-01부터 2020-09-30까지 총 트윗 개수 : ", total)
    # tweet_data = 수집한 트윗과 작성 날짜 [리스트 타입]
    
    return tweet_data