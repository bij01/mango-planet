from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        url = "mongodb://192.168.0.138:27017/"
        # url = "mongodb://localhost:27017/"
        self.mgclient = mongo_client.MongoClient(url)

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

    def return_reply(self):
        rlist = []
        nlist = []
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
                if len(rlist[x+1]) >= 100:
                    print(rlist[x], rlist[x+1])
        return nlist

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


if __name__ == "__main__":
    dm = DataManager()
    col1, col2, col3, col4, col5, col6 = dm.connect_db()
    dm.return_reply()

    # dm.drop_all()
    dm.close_db()
