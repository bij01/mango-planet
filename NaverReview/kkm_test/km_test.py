from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class ReviewCollector:
    def __init__(self):
        self.open_browser()
        self.collect_res_info("https://www.mangoplate.com/restaurants/eLq_Q72bscee")

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
        # 유승하
        click_cnt = 0
        i = 0
        k = 0
        j = 1
        link_list={}
        
        # 더보기 클릭 
        for click_cnt in range(16):
            if click_cnt < 16 :
                self.driver.find_element(By.CLASS_NAME,'btn-more').click()
                click_cnt += 1
            elif click_cnt>=16:
                break
        
        # 주소 뽑기 && 리스트 담기
        href_li = 0
        hli_add= [] # 주소를 리스트에 담기 
        while True:
            if href_li >= 300:
                break
            elif href_li < 300:
                href_li +=1
                hrefs = self.driver.find_elements(By.XPATH,'/html/body/main/article/section/div/ul/li['+str(href_li)+']/a')
                for x in hrefs:
                    href = x.get_attribute('href')
                    hli_add.append(href)
        
        # 타이틀 뽑기 && 리스트 담기
        Titles_li = 0
        Tli_add = [] # 타이틀 리스트
        while True:
            if Titles_li >= 300:
                break
            elif Titles_li < 300:
                Titles_li +=1
                Titles = self.driver.find_elements(By.XPATH,'/html/body/main/article/section/div/ul/li['+str(Titles_li)+']/a/figure/figcaption/div/span')
                for x in Titles:
                    # print(x.text)
                    Tli_add.append(x.text)
                    
        # 타이틀 및 주소 딕셔너리에 담기 
        while True:
            if j <= 300:
                link_list[Tli_add[i]] = (hli_add[k])
                i+=1; k+=1; j+=1
            else:
                break
        print(link_list['브라우니 맛집 베스트 10곳'])

                    
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
    def collect_res_info(self, url):
        # 권기민
        self.driver.get(url)
        title = self.driver.find_element(By.CSS_SELECTOR, '.restaurant_name') #식당이름
        star_rivew = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/strong')
        evaluation = self.driver.find_element(By.CSS_SELECTOR, '.cnt.favorite')
        info = self.driver.find_element(By.XPATH,'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td')
        index = info.text.index('지')
        #print(info.text[0:index-1])
        telephone_number = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td')
        price_range = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[4]/td')
        
        try:
            time.sleep(3)
            meun = self.driver.find_element(By.CLASS_NAME, 'menu_td')
            if meun.text != None:
                print(meun.text)
            else:
                pass
        except NoSuchElementException as ns:
            print("메뉴가 없습니다.")
        
        menulist = meun.find_elements(By.CLASS_NAME, "Restaurant_Menu")
        pricelist = meun.find_elements(By.CLASS_NAME, "Restaurant_MenuPrice")
        #print(len(menulist))
        lista = []
        for x in menulist:
            #print(x.text)
            lista.append(x.text)
        listb = []
        for y in pricelist:
            a = y.text.replace(',','')
            b = a.replace('원','')
            listb.append(b)
        print(listb) 
        
        title1 = title.text
        dic= {title1:{}}
        for x in range(0, len(lista)):
            k = lista[x]
            v = listb[x]
            dic[title1][k] = v
        menu_list = dic
        print(menu_list)
        
        infolist = [star_rivew.text,evaluation.text,info.text[0:index-1],telephone_number.text,str(price_range.text)]
        #print(infolist)
        info_list = {title.text:infolist}
        print(info_list)
        '''
        for title, link in res_list.items():
            #print(title, link)
            self.driver.get(link)
            info_list = {title.text:infolist}
            print(info_list)
            #menu_list = [title]=(f"{}{}")
        '''
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
