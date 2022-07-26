from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from konlpy.tag import Okt
from collections import Counter
from matplotlib import font_manager, rc

# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        url = "mongodb://192.168.0.138:27017/"
        # url = "mongodb://localhost:27017/"
        self.mgclient = mongo_client.MongoClient(url)
        font_path = "C:/Windows/Fonts/Hancom Gothic Regular.ttf"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)
    # DB 연결
    def connect_db(self):
        db = self.mgclient["restaurants"]
        self.col1 = db["link_list"]
        self.col2 = db["res_list"]
        self.col3 = db["info_list"]
        self.col4 = db["menu_list"]
        self.col5 = db["review_info_list"]
        self.col6 = db["review_list"]
        # print("DB 연결 성공")
        return self.col1, self.col2, self.col3, self.col4, self.col5, self.col6

    # Collection(table) 데이터 삽입
    def insert_data(self, col, dic):
        col.insert_one(dic)

    # Collection 데이터 확인
    def check_data(self, col):
        count = 0
        for data in col.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    count += 1
                    print(k, v)
        print(count)

    def check_data1(self, col):
        link_list = []
        for data in col.find():
            for k, v in data.items():
                if k == "link":
                    link_list.append(v)
                else:
                    pass
        return link_list

    def check_data2(self, col):
        name_list = []
        for data in col.find():
            for k, v in data.items():
                if k == "name":
                    name_list.append(v)
                else:
                    pass
        return name_list

    def drop_data(self, col):
        col.drop()

    def drop_all(self):
        # self.col1.drop()
        self.col2.drop()
        self.col3.drop()
        self.col4.drop()
        self.col5.drop()
        self.col6.drop()

    # 지역별(시단위) 맛집리스트 갯수 도표(bar chart)
    def show_localres_bchart(self):
        # x 축: 지역명, y축: 지역별 식당 갯수
        print()

    # 식당별 맛평가(맛있다, 괜찮다, 별로) 원형 도표(pie chart)
    def show_review_pchart(self):
        print()

    def close_db(self):
        self.mgclient.close()

    def return_reply(self):
        rlist = []
        nlist = []
        clist = []
        for data in col6.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    rlist.append(v)
        for x in range(0, len(rlist)):
            if x+2 > len(rlist):
                pass
            else:
                if len(rlist[x+1]) >= 150:
                    #print(rlist[x], rlist[x+1])
                    nlist.append(rlist[x]) # 식당이름
                    clist.append(rlist[x+1]) # 댓글수
        return nlist, clist

    def show_word_chart(self):
        nlist, clist = self.return_reply()
        print(len(nlist))

        for i in range(0, len(nlist)):
            #print(i,"시작")
            okt = Okt()
            noun = okt.nouns(str(clist[i]))
            for j,m in enumerate(noun):
                if len(m)<2:
                    noun.pop(j)

            count = Counter(noun)
            noun_list = count.most_common(5)

            #print(i,"중간")
            x_list = [] # 검색된 글자
            y_list = [] # 숫자
            for x, y in noun_list:
                x_list.append(x)
                y_list.append(y)
            #print(x_list) #검사
            #print(y_list) #검사
            plt.title(nlist[i])
            plt.bar(x_list, y_list, width=0.5) #color=
            plt.savefig("C:\\Users\\Kosmo\\Desktop\\JJ\\"+nlist[i]+".png", format='png', dpi=300, facecolor="white")
            plt.clf()
            #plt.show()   

if __name__ == "__main__":
    dm = DataManager()
    col1, col2, col3, col4, col5, col6 = dm.connect_db()
    dm.show_word_chart()
    # dm.check_data(col6)
    
    # dm.drop_all()
    dm.close_db()
