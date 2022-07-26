from selenium.webdriver.common.by import By
import time

# 3. 식당 별 정보 가져오기
# 1) 수집할 데이터: 식당이름, 주소, 전화번호, 음식 종류, 가격대, 메뉴, 메뉴가격
# 2) 제공 형태
# -> info_dict = {"name:식당이름", info:[별점, 별점개수, 주소, 전화번호, 음식종류, 가격대]}
# -> menu_dict = {"name:식당이름", menu:{"메뉴1":가격(int), "메뉴2":가격(int), "메뉴3":가격(int)}, ...]}
def collect_infomation(driver, url):
    # 권기민
    driver.get(url)
    driver.implicitly_wait(30)
    time.sleep(10)
    time.sleep(5)

    driver.implicitly_wait(30)
    time.sleep(10)

    driver.implicitly_wait(30)
    title = driver.find_element(By.CSS_SELECTOR, '.restaurant_name')  # 식당이름
    try:
        star_review = driver.find_element(By.XPATH,
                                               '/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/strong')
        star = star_review.text
    except:
        star = 0
    evaluation = driver.find_element(By.CSS_SELECTOR, '.cnt.favorite')
    info = driver.find_element(By.XPATH,
                                    '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td')
    index = info.text.index('지')
    telephone_number = driver.find_element(By.XPATH,
                                                '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td')
    price_range = driver.find_element(By.XPATH,
                                           '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[4]/td')
    try:
        time.sleep(1)
        menu = driver.find_element(By.CLASS_NAME, 'menu_td')
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
        menudic = {}
        for x in range(0, len(lista)):
            k = lista[x]
            v = listb[x]
            menudic[k] = v
        menu_dict = {"name": title.text, "menu": menudic}
        # print(menu_dict)
    except:
        menu_dict = {"name": title.text, "menu": {}}
    try:
        info_list = [star, evaluation.text.replace(",", ""), info.text[0:index - 1],
                     telephone_number.text,
                     str(price_range.text)]
        info_dict = {"name": title.text, "info": info_list}
    except:
        info_dict = {"name": title.text, "info": []}
    return info_dict, menu_dict