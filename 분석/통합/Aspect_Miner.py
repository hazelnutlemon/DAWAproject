# https://bab2min.tistory.com/552
def aspect_miner(work_name):
    import csv
    from konlpy.tag import Okt
    from gensim.models import word2vec

    file_name='Crawling\\' + work_name +'.txt'
    #작품 리뷰 모음을 읽는다.
    f = open(file_name, 'r', encoding='utf-8')
    data = f.read().split('.')
    f.close()

    """
    f = open("practice.txt", 'r',encoding='utf-8')
    data = f.read().split('.').replace('\n','')
    print(data)
    f.close()
    """
    character_word_list=[]
    mood_word_list=[]
    story_word_list=[]
    
    #트위터 형태소 분석기를 로드한다. Twiter가 KoNLPy v0.4.5 부터 Okt로 변경 되었다.
    twitter = Okt()

    #텍스트를 한줄씩 처리합니다.
    result = []
    for line in data:
        # 형태소 분석하기, 단어 기본형 사용
        malist = twitter.pos(line.strip(), norm=True, stem=True)
        r = []
        for word in malist:
         #Josa”, “Eomi”, “'Punctuation” 는 제외하고 처리
            #if not word[1] in ["Josa","Eomi","Punctuation"]:
            if word[1] in ["Noun","Adjective"]:
                r.append(word[0])
     #형태소 사이에 공백 " "  을 넣습니다. 그리고 양쪽 공백을 지웁니다.
        rl = (" ".join(r)).strip()
        result.append(rl)
     #print(rl)

    #형태소들을 별도의 파일로 저장 합니다.
    with open("NaverMovie.nlp",'w', encoding='utf-8') as fp:
        fp.write("\n".join(result))

    #Word2Vec 모델 만들기
    wData = word2vec.LineSentence("NaverMovie.nlp")
    wModel =word2vec.Word2Vec(wData, size=200, window=10, hs=1, min_count=2, sg=1)
    wModel.save("NaverMovie.model")
    print("Word2Vec Modeling finished")

    twitter = Okt()

    model = word2vec.Word2Vec.load("NaverMovie.model")
    count = 0
    model_list = []
    model_list = model.most_similar(positive=["주인공"], topn=300)
    for i in range(len(model_list)):
        temp_list = twitter.pos(model_list[i][0], norm=True, stem=True)
        if (temp_list[0][1] == 'Adjective'):
            character_word_list.append(temp_list[0][0])
            count += 1

        if (count == 5):
            break;
    
    count = 0
    model_list = []
    model_list = model.most_similar(positive=["스토리"], topn=300)
    for i in range(len(model_list)):
        temp_list = twitter.pos(model_list[i][0], norm=True, stem=True)
        if (temp_list[0][1] == 'Adjective'):
            story_word_list.append(temp_list[0][0])
            count += 1

        if (count == 5):
            break;
          
    count = 0        
    model_list = []
    model_list = model.most_similar(positive=["분위기"], topn=300)
    for i in range(len(model_list)):
        temp_list = twitter.pos(model_list[i][0], norm=True, stem=True)
        if (temp_list[0][1] == 'Adjective'):
            mood_word_list.append(temp_list[0][0])
            count += 1

        if (count == 5):
            break;
            
    return character_word_list,story_word_list,mood_word_list