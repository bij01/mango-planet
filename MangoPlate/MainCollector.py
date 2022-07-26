import os
import socket

from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from DataManager import DataManager as dm
from collector.review import collect_review
from collector.information import collect_infomation


class MainCollector:
    def __init__(self, mode, start_num, end_num):
        self.current = 0
        self.col1, self.col2, self.col3, \
        self.col4, self.col5, self.col6 = dm.connect_db(dm())
        self.start_num = start_num
        self.end_num = end_num
        self.mode = mode
        self.open_browser()
        if start_num is None:
            pass
        else:
            # print("DATA 수집 시작")
            self.collect_data()

    def get_current_page(self):
        return self.current

    def open_browser(self):
        path = "c:/python/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(3)
        url = "https://www.mangoplate.com/top_lists"
        self.driver.get(url)

    def close_db(self):
        dm.close_db(dm())

    def collect_data(self):
        # 백인준
        # 1. 테마별 식당 목록 수집 및 데이터 입력
        # self.collect_theme_list()
        # 2. 식당리스트 수집 및 데이터 입력
        if self.mode == 2:
            self.repeat_crawling(self.col1)
        # 3. 식당정보 및 리뷰 수집
        else:
            self.repeat_crawling(self.col2)

    def repeat_crawling(self, col):
        count = 0  # 전체 페이지
        for _ in col.find():
            count += 1
        linklist = dm.check_data1(dm(), col)
        for x in range(0, len(linklist)):
            if col == self.col1:
                # 테마별 식당 링크 목록 중에 지정된 범위내 에서만 데이터 수집
                if x not in range(self.start_num, self.end_num):
                    # print("pass", x)
                    pass
                else:
                    print(f"식당 목록 크롤링 중.. {x}/{count}")
                    self.collect_res_list(linklist[x])
                    self.current = x
            elif col == self.col2:
                # 식당 목록 중에 지정된 범위내 에서만 데이터 수집
                if x not in range(self.start_num, self.end_num):
                    # print("pass", x)
                    pass
                else:
                    print(f"식당 정보 & 댓글 크롤링 중.. {x}/{count}")
                    # 식당 데이터 수집
                    info_dict, menu_dict = collect_infomation(self.driver, linklist[x])
                    for k, v in info_dict.copy().items():
                        if k == "name":
                            if v in dm.check_data2(dm(), self.col3):
                                print(f"중복 데이터 패스 {x}, {v}")
                                pass
                            else:
                                dm.insert_data(dm(), self.col3, info_dict)
                            if v in dm.check_data2(dm(), self.col4):
                                print(f"중복 데이터 패스 {x}, {v}")
                                pass
                            else:
                                dm.insert_data(dm(), self.col4, menu_dict)

                    # 댓글 데이터 수집
                    info, review = collect_review(self.driver, linklist[x])
                    for k, v in info.copy().items():
                        if k == "name":
                            if v in dm.check_data2(dm(), self.col5):
                                print(f"중복 데이터 패스 {x}, {v}")
                                pass
                            else:
                                dm.insert_data(dm(), self.col5, info)
                            if v in dm.check_data2(dm(), self.col6):
                                print(f"중복 데이터 패스 {x}, {v}")
                                pass
                            else:
                                dm.insert_data(dm(), self.col6, review)
                    self.current = x
            else:
                pass

    # 1. 맛집 베스트 XX곳 목록 정보 가져오기
    # 1) 수집할 데이터: 타이틀, 타이틀링크
    # 2) 목표데이터: 300개
    # -> link_list = {title:"테마이름", link:"링크주소"}
    def collect_theme_list(self):
        # 유승하
        input("팝업창 닫고 ENTER")
        print("테마별 식당 리스트 수집 시작")
        i, k, j = 0, 0, 1
        self.link_list = {}

        # 더보기 클릭
        for click_cnt in range(16):
            if click_cnt < 16:
                self.driver.find_element(By.CLASS_NAME, 'btn-more').click()
                click_cnt += 1
            elif click_cnt >= 16:
                break

        # 주소 뽑기 && 리스트 담기
        href_li = 0
        hli_add = []  # 주소를 리스트에 담기
        while True:
            if href_li >= 300:
                break
            elif href_li < 300:
                href_li += 1
                hrefs = self.driver.find_elements(By.XPATH,
                                                  '/html/body/main/article/section/div/ul/li[' + str(href_li) + ']/a')
                for x in hrefs:
                    href = x.get_attribute('href')
                    hli_add.append(href)

        # 타이틀 뽑기 && 리스트 담기
        Titles_li = 0
        Tli_add = []  # 타이틀 리스트
        while True:
            if Titles_li >= 300:
                break
            elif Titles_li < 300:
                Titles_li += 1
                Titles = self.driver.find_elements(By.XPATH, '/html/body/main/article/section/div/ul/li[' + str(
                    Titles_li) + ']/a/figure/figcaption/div/span')
                for x in Titles:
                    # print(x.text)
                    Tli_add.append(x.text)

        # 타이틀 및 주소 딕셔너리에 담기
        while True:
            if j <= 300:
                if Tli_add[i] in dm.check_data2(dm(), self.col1):
                    pass
                else:
                    self.link_list = {"title": Tli_add[i], "link": hli_add[k]}
                    dm.insert_data(dm(), self.col1, self.link_list)
                i += 1
                k += 1
                j += 1
            else:
                break

        print("테마별 식당 리스트 수집 종료")

    # 2. 맛집리스트 별 식당정보 가져오기
    # 1) 수집할 데이터: 식당목록, 식당상세페이지 링크, 사진(식당이름+.jpg)
    # 2) 요구사항: 사진은 xx 맛집 베스트 폴더안에 저장
    # -> res_list = {name:"식당이름", link:"링크주소"}
    def collect_res_list(self, url):
        # 박종원
        self.driver.get(url)

        while True:
            try:
                more = self.driver.find_element(By.CLASS_NAME, "more_btn")
                more.click()
            except:
                break
        info = self.driver.find_elements(By.CLASS_NAME, "info")
        # print(info)
        i = -1

        for _ in info:
            try:
                i = i + 1
                # print(info[i].find_element(By.TAG_NAME, "a").text[3:].strip())
            except:
                break
        imgs = self.driver.find_elements(By.CLASS_NAME, "center-croping.lazy")

        lastnum = 0
        items = self.driver.find_elements(By.CLASS_NAME, "restaurant-item")
        # print(lastnum)
        if not os.path.isdir("imgs"):
            # print("폴더 생성 완료")
            os.mkdir("imgs")
        else:
            # print("동일한 폴더 존재")
            pass
        for item in items:
            text = item.find_element(By.CLASS_NAME, "title ").text
            imglink = item.find_element(By.TAG_NAME, "img").get_attribute("data-original")
            try:
                int(text[0])
                lastnum += 1
                # print(text, imglink)
                socket.setdefaulttimeout(10)
                try:
                    # print("이미지 다운로드 시도")
                    request.urlretrieve(imglink, "imgs/" + text[3:].strip() + '.jpg')
                    # print("다운로드 성공")
                except:
                    # print("다운로드 실패")
                    continue
            except:
                pass

        info = self.driver.find_elements(By.CLASS_NAME, "info")
        i = -1

        lista = []
        for abc in info:
            try:
                i = i + 1
                # print(info[i].find_element(By.TAG_NAME, "a").text[3:].strip())
                lista.append(info[i].find_element(By.TAG_NAME, "a").text[3:].strip())
            except:
                break
        # print(lista)

        listb = []
        for x in range(1, int(lastnum) + 1):
            link = self.driver.find_elements(By.XPATH, '//*[@id="contents_list"]/ul/li[' + str(
                x) + ']/div/figure/figcaption/div/span/a')
            for y in link:
                href = y.get_attribute('href')
                listb.append(href)
        # print(listb)

        dic = {}
        for x1 in range(0, len(lista)):
            k = lista[x1]
            v = listb[x1]
            dic[k] = v
            for k, v in dic.items():
                # 중복 식당 링크일 경우 패스
                if v in dm.check_data1(dm(), self.col2):
                    pass
                else:
                    new_dic = {"name": k, "link": v}
                    dm.insert_data(dm(), self.col2, new_dic)


