import time

from pymongo import mongo_client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ReviewCollector:
    def __init__(self):
        self.connect_db()
        self.open_browser()
        self.collect_theme_list()

    def open_browser(self):
        path = "c:/python/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(3)
        url = "https://www.mangoplate.com/top_lists"
        self.driver.get(url)

    def collect_data(self):
        # 백인준 (합칠거)
        print()

    # 1. 맛집 베스트 XX곳 목록 정보 가져오기
    # 1) 수집할 데이터: 타이틀, 타이틀링크
    # 2) 목표데이터: 300개
    # 3) 목적: 수집한 데이터를 2번 함수에 제공
    # 4) 가공 형태
    # -> link_list = {"타이틀1":"링크주소", "타이틀2":"링크주소", "타이틀3":"링크주소" ...}
    def collect_theme_list(self):
        input("팝업창 닫고 ENTER")
        # 유승하
        i = 0
        k = 0
        j = 1
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


    def change_review_page(self):
        # btn1 맛있다, btn2 괜찮다, btn3 별로
        btn1 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__RecommendFilterButton')
        btn2 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__OkFilterButton')
        # 별로의 개수가 없으면 넘어가지 않음

        btn3 = self.driver.find_element(By.CSS_SELECTOR,'.RestaurantReviewList__FilterButton.RestaurantReviewList__NotRecommendButton') #별로

        review_cnt = self.driver.find_element(By.XPATH,"/html/body/main/article/div[1]/div[1]/div/section[3]/header/h2/span[4]")
        if str(review_cnt) == str(30): # 리뷰 개수(bb)와 30개 비교
            pass
            #btn1.click()
        else:
            pass

        btn3 = self.driver.find_element(By.CSS_SELECTOR,
                                        '.RestaurantReviewList__FilterButton.RestaurantReviewList__NotRecommendButton')
        review_cnt = self.driver.find_element(By.XPATH,
                                              "/html/body/main/article/div[1]/div[1]/div/section[3]/header/h2/span[4]")
        if str(review_cnt) == str(30):  # 리뷰 개수(bb)와 30개 비교
            btn1.click()
        else:
            pass

    # 2. 맛집리스트 별 식당정보 가져오기
    # 1) 수집할 데이터: 식당목록, 식당상세페이지 링크, 사진(식당이름+.jpg)
    # 2) 요구사항: 사진은 xx 맛집 베스트 폴더안에 저장
    # 3) 목적: 식당목록, 식당상세페이지 링크를 3번 함수에 제공
    # 4) 가공 형태
    # -> res_list = {"식당이름1":"링크주소", "식당이름2":"링크주소", "식당이름3":"링크주소" ...}
    def collect_res_list(self):
        # 박종원
        # for title, link in self.link_list.items():
        #     print(title, link)
        #     # self.driver.get(link)
        print()

    # 3. 식당 별 정보 가져오기
    # 1) 수집할 데이터: 식당이름, 주소, 전화번호, 음식 종류, 가격대, 메뉴, 메뉴가격
    # 2) 가공 형태
    # -> info_list = {"식당이름":[별점, 별점개수, 주소, 전화번호, 음식종류, 가격대]}
    # -> menu_list = {"식당이름":{"메뉴1":가격(int), "메뉴2":가격(int), "메뉴3":가격(int)}, ...]}
    def collect_res_info(self):
        # 권기민
        # for title, link in res_list.items():
        #     print(title, link)
        #     driver.get(link)
        print()

    # 4. 식당 별 리뷰정보 가져오기
    # 1) 수집할 데이터: 식당이름, 리뷰갯수, (갯수)맛있다, 괜찮다, 별로, 리뷰내용
    # 2) 가공 형태
    # -> review_list = {"식당이름", [리뷰갯수(int), 맛있다(int), 괜찮다(int), 별로(int), 리뷰내용(str)]}
    def collect_res_reviews(self):
        # 지예성
        t = 1
        # 더보기 클릭
        while True:
            try:
                btn = self.driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                t += 1
                if t == 10:
                    break
            except:
                break
        time.sleep(2)
        i = 1
        while True:
            try:
                selector = "body > main > article > div.column-wrapper > div.column-contents " \
                           "> div > section.RestaurantReviewList " \
                           "> ul > li:nth-child(" + str(i) + ") > a"
                self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(Keys.ENTER)  # 댓글 클릭
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                comment = self.driver.find_element(By.CLASS_NAME, "ReviewCard__ReviewText").text
                print(comment)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                i += 1
            except:
                break
        print()

    # DB 연결
    def connect_db(self):
        url = "mongodb://localhost:27017/"
        mgclient = mongo_client.MongoClient(url)
        db = mgclient["restaurants"]
        self.col1 = db["link_list"]
        self.col2 = db["res_list"]
        self.col3 = db["info_list"]
        self.col4 = db["menu_list"]
        self.col5 = db["review_list"]

    # Collection(table) 데이터 삽입
    def insert_data(self, col, dic):
        for key, value in dic.items():
            new_dic = {key: value}
            col.insert_one(new_dic)

    # Collection 데이터 확인
    def check_data(self, col):
        for data in col.find():
            print(data)


if __name__ == "__main__":
    ReviewCollector()
