import os
from collections import Counter

import seaborn as sns
from konlpy.tag import Okt
from matplotlib import font_manager, rc
from matplotlib import pyplot as plt
from pymongo import mongo_client

from collector.longname_chart import save_longname_chart


# 모든 도표는 파일로 저장


class DataManager:
    def __init__(self):
        url = "mongodb://192.168.0.138:27017/"
        # url = "mongodb://localhost:27017/"

        self.mgclient = mongo_client.MongoClient(url)
        # 도표 한글 깨짐 방지
        font_path = "C:/windows/Fonts/malgun.ttf"
        font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family='Malgun Gothic', size=10)

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
            if x + 2 > len(rlist):
                pass
            else:
                if len(rlist[x + 1]) >= 100:
                    print(rlist[x], rlist[x + 1])
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

    def make_folders(self):
        path1 = "imgs/chart/taste/"
        path2 = "imgs/chart/review/"
        if not os.path.exists(path1):
            os.makedirs(path1)
        if not os.path.exists(path2):
            os.makedirs(path2)

    # 지역별(시단위) 맛집리스트 갯수 도표(bar chart)
    def show_localres_bchart(self):
        # x 축: 지역별 식당 갯수, y축: 지역명
        path = "imgs/chart/"
        data_c = list()
        # colors = ["red", "green", "blue", "yellow", "pink", "orange", "cyan", "hotpink", "black", "magenta"]
        for x in self.col3.find():
            data = x['info']
            a = data[2]
            b = a.split()
            c = b[0]
            data_c.append(c)
            # print(c)

        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        y = ['서울특별시', '경기도', '제주특별자치도', '강원도', '부산광역시', '전라남도', '인천광역시', '대전광역시', '경상북도', '충청남도', '경상남도', '광주광역시',
             '대구광역시', '전라북도', '충청북도', '울산광역시']

        for x in data_c:
            for j in range(0, 16):
                if x == y[j]:
                    s[j] = s[j] + 1
        # print(s)

        s_squared = list()
        for i in range(0, len(s)):
            s_squared.append(s[i] ** (1 / 2))
        colors = sns.color_palette('autumn', len(y))
        plt.barh(y, s_squared, color=colors)
        plt.xticks([0, 20, 49], [0, s[1], s[0]])
        plt.title('지역별 맛집 분포도', loc='center')
        plt.savefig(path + "count_local.png", format='png', dpi=300, facecolor="white")
        plt.close()

    # 가격별 가게 분포도
    def save_price_range_chart(self):
        path = "imgs/chart/"
        data_a = list()
        exlist = ["주차공간없음", "무료주차", "유료주차", "감자송편", "식당", "12:00", "11:00", "멍게젓비빔밥", "선어사시미", "발렛", "특수부위",
                  "한우특수부위(160g)"]
        for x in self.col3.find():
            data = x['info']
            price_range = data[4]
            if len(price_range) == 0:
                pass
            else:
                price = price_range.split()[0]
                if price in exlist:
                    pass
                else:
                    data_a.append(price)
                    # print(price)
        s = [0, 0, 0, 0, 0]
        y = ["만원", "만원-2만원", "2만원-3만원", "4만원", "3만원-4만원"]
        for x in data_a:
            for j in range(0, 5):
                if x == y[j]:
                    s[j] = s[j] + 1

        colors = sns.color_palette('autumn', len(y))
        plt.bar(y, s, color=colors, width=0.6)
        plt.title('맛집리스트 별 평균 가격대', loc='center')
        plt.savefig(path + "price_range.png", format='png', dpi=300, facecolor="white")
        plt.close()

    # 식당별 맛평가(맛있다, 괜찮다, 별로) 원형 도표(pie chart)
    def save_review_chart(self, col):
        totalcount = 0
        for data in col.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    totalcount += 1
        pimg_path = "imgs/chart/taste/"
        count = 0
        print("도표 생성 중 입니다 잠시만 기다려주세요")
        for data in col.find():
            for k, v in data.items():
                if k == "_id":
                    pass
                else:
                    print(f"도표 생성 중.. {count + 1}/{totalcount}")
                    count += 1
                    if k == "name":
                        img_name = v
                        title = v
                    if k == "count":
                        ratio = [v[1], v[2], v[3]]
                        labels = ['맛있다', '괜찮다', '별로']
                        colors = ['#ff9999', '#ffc000', '#8fd9b6']
                        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 4}
                        explode = [0, 0.10, 0.07]
                        _, _, autotexts = plt.pie(ratio, autopct='%.1f%%', shadow=True, startangle=260, pctdistance=1.2,
                                                  counterclock=False, colors=colors, wedgeprops=wedgeprops,
                                                  explode=explode, radius=1.0)
                        plt.legend(labels, loc='center left', bbox_to_anchor=(1, 1))
                        for autotext in autotexts:
                            autotext.set_color('black')
                            autotext.set_fontsize('14')
                        plt.title(title, fontsize=20, pad=15)
                        plt.savefig(pimg_path + img_name + ".png", format='png', dpi=300, facecolor="white")
                        plt.close()
        print("도표 생성 완료")

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
            if x + 2 > len(rlist):
                pass
            else:
                if len(rlist[x + 1]) >= 100:
                    # print(rlist[x], rlist[x+1])
                    nlist.append(rlist[x])
                    clist.append(rlist[x + 1])
        return nlist, clist

    def show_word_chart(self):
        nlist, clist = self.return_reply()
        print("차트 생성 중 입니다 잠시만 기다려주세요")
        for i in range(0, len(nlist)):
            print(f"차트 생성 중.. {i + 1}/{len(nlist)}")
            # print(i,"시작")
            okt = Okt()
            noun = okt.nouns(str(clist[i]))
            for j, m in enumerate(noun):
                if len(m) < 2:
                    noun.pop(j)

            count = Counter(noun)
            noun_list = count.most_common(5)
            colors = ['red', 'orange', 'purple', 'blue', 'green']
            x_list = []  # 검색된 글자
            y_list = []  # 숫자
            for x, y in noun_list:
                x_list.append(x)
                y_list.append(y)
            plt.title(nlist[i])
            plt.bar(x_list, y_list, width=0.5, color=colors, edgecolor='black')
            plt.savefig("imgs/chart/review/" + nlist[i] + ".png", format='png', dpi=300, facecolor="white")
            plt.clf()
        print("차트 생성 완료")


if __name__ == "__main__":
    dm = DataManager()
    col1, col2, col3, col4, col5, col6 = dm.connect_db()

    dm.make_folders()  # imgs 폴더 만들기(서브 폴더 포함)
    # save_longname_chart()  # 이름이 긴 식당 TOP5 (1장)
    # dm.save_price_range_chart()  # 가격별 차트 (1장)
    dm.show_localres_bchart()  # 지역별 식당 분포 차트 (1장)
    # dm.save_review_chart(col5)  # 식당별 맛평가 차트 (여러장)
    # dm.show_word_chart()  # 댓글이 n개 이상인 식당의 댓글내용 분석 차트 (여러장)

    dm.close_db()
