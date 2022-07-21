from urllib import request
from matplotlib.pyplot import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "c:/python/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
url = "https://www.mangoplate.com/top_lists"
driver.get(url)

'''
def click_viewmore():
    driver.find_element(By.CLASS_NAME,'btn-more').click() 
'''

titles = driver.find_elements(By.CSS_SELECTOR,'.top_list_item')
for x in titles:
    print(x.text)
        



