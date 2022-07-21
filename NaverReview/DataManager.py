from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        print()

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
            print(data)

    # 지역별(시단위) 맛집리스트 갯수 도표(bar chart)
    def show_localres_bchart(self):
        # x 축: 지역명, y축: 지역별 식당 갯수
        print()

    # 식당별 맛평가(맛있다, 괜찮다, 별로) 원형 도표(pie chart)
    def show_review_pchart(self):
        print()

    #


if __name__ == "__main__":
    DataManager()
