from pymongo import mongo_client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import font_manager, rc
import os
# 모든 도표는 파일로 저장


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
                        print("해당 경로에 폴더가 없습니다. 생성합니다 ")
                        os.makedirs(pimg_path)
                    else:
                        plt.savefig(pimg_path+img_name+".png",format='png',dpi=300, facecolor="white")
                        plt.clf()