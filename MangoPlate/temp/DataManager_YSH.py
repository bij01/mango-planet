from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import font_manager, rc
import os
# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        url = "mongodb://192.168.0.138:27017/"
        # url = "mongodb://localhost:27017/"
        self.mgclient = mongo_client.MongoClient(url)
        # 도표 한글 깨짐 방지
        font_path = "C:/Windows/Fonts/MalangmalangB.TTF"
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


    # 식당별 맛평가(맛있다, 괜찮다, 별로) 원형 도표(pie chart)
    def show_review_pchart(self,col):
        pimg_path = "C:/Users/Kosmo/Desktop/Test/"
        count = 0
        for data in col.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    count += 1
                    if k == "name":
                        img_name = v
                    if k == "count":
                        ratio = [v[1], v[2], v[3]]
                        labels = ['맛있다', '괜찮다', '별로']
                        colors = ['#ff9999', '#ffc000', '#8fd9b6']
                        wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 4}
                        explode = [0, 0.10, 0.07]
                        _,_, autotexts = plt.pie(ratio, autopct='%.1f%%',shadow=True, startangle=260, pctdistance=1.2, counterclock=False, colors=colors, wedgeprops=wedgeprops, explode=explode, radius=1.0)
                        plt.legend(labels, loc='center left', bbox_to_anchor=(0.9,0.9))
                        for autotext in autotexts:
                            autotext.set_color('black')
                            autotext.set_fontsize('14')
                        if not os.path.exists(pimg_path):
                            print("")
                            os.makedirs(pimg_path)
                        else:
                            plt.savefig(pimg_path+img_name+".png",format='png',dpi=300, facecolor="white")
                            plt.clf()
                                      
        #def close_db(self):
        #    self.mgclient.close()


if __name__ == "__main__":
    dm = DataManager()
    col1, col2, col3, col4, col5, col6 = dm.connect_db()
    
    #name = dm.check_data2(col2)
    #print(name)
    dm.show_review_pchart(col5)
    # dm.drop_all()
    dm.close_db()
