from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "c:/python/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
url = "https://www.mangoplate.com/top_lists"
driver.get(url)
link_list={}


click_cnt = 0 #클릭 횟수
for click_cnt in range(16):
    if click_cnt < 16 :
        driver.find_element(By.CLASS_NAME,'btn-more').click()
        click_cnt += 1
    elif click_cnt>=16:
        break

href_li = 0 # 주소 갯수
while True:
    if href_li >= 10:
        break
    elif href_li < 10:
        href_li +=1
        herfs = driver.find_elements(By.XPATH,'/html/body/main/article/section/div/ul/li['+str(href_li)+']/a')
        for x in herfs:
            href = x.get_attribute('href')
            print(href)
            
Titles_li = 0 # 타이틀 갯수
while True:
    if Titles_li >= 10:
        break
    elif Titles_li < 10:
        Titles_li +=1
        Titles = driver.find_elements(By.XPATH,'/html/body/main/article/section/div/ul/li['+str(Titles_li)+']/a/figure/figcaption/div/span')
        for x in Titles:
            print(x.text)

link_list[x.text]=(href)
print(link_list[0])