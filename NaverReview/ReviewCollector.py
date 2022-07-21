from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ReviewCollector:
    def __init__(self):
        self.open_browser()

    def open_browser(self):
        path = "c:/python/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(3)
        url = "http://map.naver.com/v5/search/%EA%B0%80%EC%82%B0%EB%8F%99%EB%A7%9B%EC%A7%91?c=14125057.2647629,4505791.9329055,15,0,0,0,dh"
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
        # 유승하
        print()

    # 2. 맛집리스트 별 식당정보 가져오기
    # 1) 수집할 데이터: 식당목록, 식당상세페이지 링크, 사진(식당이름+.jpg)
    # 2) 요구사항: 사진은 xx 맛집 베스트 폴더안에 저장
    # 3) 목적: 식당목록, 식당상세페이지 링크를 3번 함수에 제공
    # 4) 가공 형태
    # -> res_list = {"식당이름1":"링크주소", "식당이름2":"링크주소", "식당이름3":"링크주소" ...}
    def collect_res_list(self):
        # 박종원
        # for title, link in link_list.items():
        #     print(title, link)
        #     driver.get(link)
        print()

    # 3. 식당 별 정보 가져오기
    # 1) 수집할 데이터: 식당이름, 주소, 전화번호, 음식 종류, 가격대, 메뉴, 메뉴가격
    # 2) 가공 형태
    # -> info_list = {"식당이름":[별점, 별점개수, 주소, 전화번호, 음식종류, 가격대], ...}
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
        print()

    def connect_db(self):
        print()


if __name__ == "__main__":
    ReviewCollector()