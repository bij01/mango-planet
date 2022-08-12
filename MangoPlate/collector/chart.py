from pymongo import MongoClient
from konlpy.tag import Okt
from collections import Counter


def connect_db():
    client = MongoClient(host='localhost', port=27017)
    db = client['restaurants']
    return db, client


def input_data(name):
    db, client = connect_db()
    chart_col = db["review_chart"]
    review_col = db["review_list"]
    data = review_col.find_one({"name": name})
    if data is None:
        print("댓글이 없습니다.")
        pass
    else:
        comment_list = data["comment"]
        okt = Okt()
        noun = okt.nouns(str(comment_list))
        for j, m in enumerate(noun):
            if len(m) < 2:
                noun.pop(j)
        count = Counter(noun)
        noun_list = count.most_common(5)
        x_list = []  # 검색된 글자
        y_list = []  # 숫자
        for x, y in noun_list:
            x_list.append(x)
            y_list.append(y)
        if chart_col.find_one({"name": name}) is None:
            chart_col.insert_one({"name": name, "x_list": x_list, "y_list": y_list})
            print(f'{name} 데이터 입력 성공')
        else:
            print("중복된 데이터 입니다.")
    client.close()


# input_data("왕스덕")
def loop_input_data():
    db, client = connect_db()
    col = db["review_list"]
    for data in col.find().sort("_id"):
        input_data(data["name"])


loop_input_data()

