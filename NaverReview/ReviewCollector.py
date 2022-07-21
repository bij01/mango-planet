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

    def collect_review(self):
        # 백인준 (합칠거)
        print()

    def collect_review1(self):
        # 박종원
        print()

    def collect_review2(self):
        # 유승하
        print()

    def collect_review3(self):
        # 권기민
        print()

    def collect_review4(self):
        # 지예성
        print()


