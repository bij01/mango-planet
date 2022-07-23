import os
import socket
import time
from urllib import request

from selenium import webdriver
from selenium.webdriver.common.by import By

from DataManager import DataManager as dm
from sub.SubCollector import collect_res_reviews


class ReviewCollector:
    def __init__(self, start_num, end_num, mode):
        self.col1, self.col2, self.col3, \
        self.col4, self.col5, self.col6 = dm.connect_db(dm())
        self.start_num = start_num
        self.end_num = end_num
        self.mode = mode
        self.open_browser()
        if start_num is None:
            pass
        else:
            print("DATA 수집 시작")
            try:
                self.collect_data()
            except:
                pass

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
        # 1. 테마별 식당 리스트 수집 및 데이터 입력
        # self.collect_theme_list()
        # 2. 식당리스트 수집 및 데이터 입력
        if self.mode == 2:
            self.repeat_crawling(self.col1)
        # 3. 식당정보 및 리뷰 수집
        else:
            self.repeat_crawling(self.col2)

    def repeat_crawling(self, col):
        x = 0
        count = 0
        for _ in col.find():
            count += 1
        for data in col.find():
            for key, value in data.items():
                if key == "_id":
                    pass
                else:
                    if col == self.col1:
                        # 테마별 식당 링크 목록 중에 지정된 범위내 에서만 데이터 수집
                        if x not in range(self.start_num, self.end_num):
                            # print("pass", x)
                            pass
                        else:
                            print(f"식당 리스트 크롤링 중.. {x}/{count}")
                            self.collect_res_list(value)
                    if col == self.col2:
                        # 식당 목록 중에 지정된 범위내 에서만 데이터 수집
                        if x not in range(self.start_num, self.end_num):
                            # print("pass", x)
                            pass
                        else:
                            print(f"식당 정보, 리뷰 크롤링 중.. {x}/{count}")
                            self.collect_res_info(value)
                            info, review = collect_res_reviews(driver=self.driver, url=value)
                            if info in dm.check_data2(dm(), self.col5):
                                pass
                            else:
                                dm.insert_data(dm(), self.col5, info)
                                dm.insert_data(dm(), self.col6, review)
                    else:
                        pass
                    x += 1

    # 1. 맛집 베스트 XX곳 목록 정보 가져오기
    # 1) 수집할 데이터: 타이틀, 타이틀링크
    # 2) 목표데이터: 300개
    # 3) 제공 형태
    # -> link_list = {"타이틀1":"링크주소", "타이틀2":"링크주소", "타이틀3":"링크주소" ...}
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
                self.link_list[Tli_add[i]] = (hli_add[k])
                i += 1
                k += 1
                j += 1
            else:
                break

        dm.insert_data(dm(), self.col1, self.link_list)
        print("테마별 식당 리스트 수집 종료")

    def change_review_page(self):
        # btn1 맛있다, btn2 괜찮다, btn3 별로
        btn1 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__RecommendFilterButton')
        btn2 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__OkFilterButton')
        # 별로의 개수가 없으면 넘어가지 않음
        btn3 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__NotRecommendButton')  # 별로

        review_cnt = self.driver.find_element(By.XPATH,
                                              "/html/body/main/article/div[1]/div[1]/div/section[3]/header/h2/span[4]")
        if str(review_cnt) == str(30):  # 리뷰 개수(bb)와 30개 비교
            pass
            # btn1.click()
        else:
            pass

    # 2. 맛집리스트 별 식당정보 가져오기
    # 1) 수집할 데이터: 식당목록, 식당상세페이지 링크, 사진(식당이름+.jpg)
    # 2) 요구사항: 사진은 xx 맛집 베스트 폴더안에 저장
    # 3) 제공 형태
    # -> res_list = {"식당이름":"링크주소"}
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
                if v in dm.check_data2(dm(), self.col2):
                    pass
                else:
                    new_dic = {k: v}
                    dm.insert_data(dm(), self.col2, new_dic)

    # 3. 식당 별 정보 가져오기
    # 1) 수집할 데이터: 식당이름, 주소, 전화번호, 음식 종류, 가격대, 메뉴, 메뉴가격
    # 2) 제공 형태
    # -> info_dict = {"식당이름":[별점, 별점개수, 주소, 전화번호, 음식종류, 가격대]}
    # -> menu_dict = {"식당이름":{"메뉴1":가격(int), "메뉴2":가격(int), "메뉴3":가격(int)}, ...]}
    def collect_res_info(self, url):
        # 권기민
        self.driver.get(url)
        title = self.driver.find_element(By.CSS_SELECTOR, '.restaurant_name')  # 식당이름
        star_review = self.driver.find_element(By.XPATH,
                                               '/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/strong')
        evaluation = self.driver.find_element(By.CSS_SELECTOR, '.cnt.favorite')
        info = self.driver.find_element(By.XPATH,
                                        '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td')
        index = info.text.index('지')
        # print(info.text[0:index-1])
        telephone_number = self.driver.find_element(By.XPATH,
                                                    '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td')
        price_range = self.driver.find_element(By.XPATH,
                                               '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[4]/td')
        try:
            time.sleep(3)
            menu = self.driver.find_element(By.CLASS_NAME, 'menu_td')
            menulist = menu.find_elements(By.CLASS_NAME, "Restaurant_Menu")
            lista = []
            for x in menulist:
                # print(x.text)
                lista.append(x.text)
            pricelist = menu.find_elements(By.CLASS_NAME, "Restaurant_MenuPrice")
            # print(len(menulist))

            listb = []
            for y in pricelist:
                a = y.text.replace(',', '')
                b = a.replace('원', '')
                listb.append(b)
            # print(listb)

            dic = {title.text: {}}
            for x in range(0, len(lista)):
                k = lista[x]
                v = listb[x]
                dic[title.text][k] = v
            menu_dict = dic
            # print(menu_dict)
        except:
            menu_dict = {title.text: []}
        info_list = [star_review.text, evaluation.text.replace(",", ""), info.text[0:index - 1],
                     telephone_number.text,
                     str(price_range.text)]
        info_dict = {title.text: info_list}

        if title.text in dm.check_data2(dm(), self.col3):
            pass
        else:
            dm.insert_data(dm(), self.col3, info_dict)
            dm.insert_data(dm(), self.col4, menu_dict)
