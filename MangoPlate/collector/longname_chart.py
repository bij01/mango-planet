from pymongo import mongo_client
from matplotlib import pyplot as plt
import numpy as np
import re
from matplotlib import rc
from matplotlib import font_manager

url = 'mongodb://192.168.0.138:27017'
mgclient = mongo_client.MongoClient(url)

db = mgclient["restaurants"]
col2 = db["res_list"]


def return_name_list():
    # 데이터 체크 및 리스트화
    name = []
    name_len = []
    for data in col2.find():
        for k, v in data.items():
            if k == "name":
                name.append(v)
                name_len.append(len(v))

    # 리스트 초기화
    namelist = []

    # 영어제외 12글자 이상 식당 이름 리스트화
    reg = re.compile(r'[a-zA-Z]')
    for x in range(0, len(name)):
        if name_len[x] >= 12:
            if reg.findall(name[x]):
                pass
            else:
                if name[x].find("휴업중") != -1:
                    pass
                else:
                    namelist.append(str(len(name[x])) + "," + name[x])
    # 내림차순 정렬
    namelist.sort(reverse=True)

    # 오름차순 정렬
    namelist2 = []
    # 이름, 길이 리스트 추가
    for x in range(0, 5):
        namelist2.append(namelist[x])

    namelist2.sort()
    # 이름, 길이 리스트 초기화
    nlist = []
    lenlist = []
    for x in range(0, 5):
        nlist.append(namelist2[x].split(",")[1])
        lenlist.append(int(namelist2[x].split(",")[0]))
    return nlist, lenlist


def save_longname_chart():
    nlist, lenlist = return_name_list()
    f_path = "C:/windows/Fonts/malgun.ttf"
    font_manager.FontProperties(fname=f_path).get_name()
    rc('font', family='Malgun Gothic', size=10)

    y = np.arange(5)
    xlist = [0, 5, 10, 15, 20]
    colors = ['red', 'orange', 'purple', 'blue', 'green']

    plt.yticks(y, nlist)
    plt.xticks(xlist)
    plt.barh(y, lenlist, height=0.6, color=colors, edgecolor='black')
    plt.title("식당 이름 길이")
    plt.tight_layout()
    plt.savefig('imgs/chart/longname_top5.png', dpi=300, facecolor="#FFFFFF")
    plt.close()

