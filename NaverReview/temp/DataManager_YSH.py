from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        self.connect_db()
        # self.drop_data(self.col1)
        self.check_data(self.col1)
        self.show_review_pchart()


    # DB 연결
    def connect_db(self):
        url = "mongodb://localhost:27017/"
        mgClient = mongo_client.MongoClient(url)
        db = mgClient["restaurants"]
        self.col1 = db["link_list"]
        self.col2 = db["res_list"]
        self.col3 = db["info_list"]
        self.col4 = db["menu_list"]
        self.col5 = db["review_list"]

    # Collection 데이터 확인
    def check_data(self, col):
        for data in col.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    print(k, v)

    def drop_data(self, col):
        col.drop()

    # 지역별(시단위) 맛집리스트 갯수 도표(bar chart)
    def show_localres_bchart(self):
        # x 축: 지역명, y축: 지역별 식당 갯수
        print()

    # 식당별 맛평가(맛있다, 괜찮다, 별로) 원형 도표(pie chart)
    # def show_review_pchart(self):
    #    print()

    # base
    def show_review_pchart(self):
        path="C:/Users/Kosmo/Desktop/Test/"
        plt.rcParams['font.family'] = 'Hancom MalangMalang' 
        plt.rc('font', size=18)

        ratio = [34, 32, 16]
        labels = ['맛있다', '괜찮다', '별로']
        colors = ['#C70415', '#FF8500', '#6B1590']
        wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 4} # 부채꼴 모양설정 (가운데 원형 지름, 테두리 색상, 줄 굵기)
        explode = [0, 0.10, 0]
        
        _,_, autotexts = plt.pie(ratio, labels=labels, shadow=True, autopct='%.1f%%', startangle=270, counterclock=False, colors=colors, wedgeprops=wedgeprops, explode=explode)


        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize('16')
        # plt.savefig(path+"test.png",format='png',dpi=300, facecolor="white") # 이미지 저장
        plt.show()
        
        
if __name__ == "__main__":
    DataManager()
