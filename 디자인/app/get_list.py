import pymysql
from app import main_dbconn

def get_contentList(searchcontent, name2):
    conn = main_dbconn.get_connection()
    cursor = conn.cursor()
    if len(name2) < 1:
        sql = " SELECT novel.*, author.name, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5, \
                    aspect_character.reaction1, aspect_character.reaction2, aspect_character.reaction3, aspect_character.reaction4, aspect_character.reaction5, \
                    aspect_mood.reaction1, aspect_mood.reaction2, aspect_mood.reaction3, aspect_mood.reaction4, aspect_mood.reaction5, aspect_story.reaction1, aspect_story.reaction2, aspect_story.reaction3, aspect_story.reaction4, aspect_story.reaction5  \
                    FROM novel \
                    INNER JOIN textrank ON novel.idnovel = textrank.novel \
                    INNER JOIN author ON textrank.novel = author.novel \
                    INNER JOIN aspect_character ON author.novel = aspect_character.novel \
                    INNER JOIN aspect_mood ON aspect_character.novel = aspect_mood.novel \
                    INNER JOIN aspect_story ON aspect_mood.novel = aspect_story.novel \
                      where novel.title like '%" + searchcontent + "%'"
    else:
        sql = " SELECT novel.*, author.name, textrank.word1, textrank.word2, textrank.word3, textrank.word4, textrank.word5, \
                    aspect_character.reaction1, aspect_character.reaction2, aspect_character.reaction3, aspect_character.reaction4, aspect_character.reaction5, \
                    aspect_mood.reaction1, aspect_mood.reaction2, aspect_mood.reaction3, aspect_mood.reaction4, aspect_mood.reaction5, aspect_story.reaction1, aspect_story.reaction2, aspect_story.reaction3, aspect_story.reaction4, aspect_story.reaction5  \
                    FROM novel \
                    INNER JOIN textrank ON novel.idnovel = textrank.novel \
                    INNER JOIN author ON textrank.novel = author.novel \
                    INNER JOIN aspect_character ON author.novel = aspect_character.novel \
                    INNER JOIN aspect_mood ON aspect_character.novel = aspect_mood.novel \
                    INNER JOIN aspect_story ON aspect_mood.novel = aspect_story.novel \
                    where novel.title like" + "'%" + name2 + "%'" + "and novel.publisher like '%" + searchcontent + "%'"

    cursor.execute(sql)
    row = cursor.fetchall()

    contentList = []

    for obj in row :
        data_list = {
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
        contentList.append(data_list)

    conn.close

    return contentList