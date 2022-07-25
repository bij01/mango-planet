from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


def collect_review(driver, url):
    # 지예성
    driver.implicitly_wait(5)
    restaurantname = driver.find_element(By.CLASS_NAME,"restaurant_name").text
    # print(restaurantname)

    driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(2) > button").send_keys(Keys.ENTER)
    oldcountB, newcountB = None, 0
    # 더보기 클릭
    while True:
        try:
            # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
            if oldcountB == newcountB:
                # print("old:", oldcountB, "new:", newcountB)
                break
            else:
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                oldcountB = len(reviews)
                # print("old:", oldcountB)
                btn = driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                newcountB = len(reviews)
                # print("new:", newcountB)
                # print()
        except:
            break

    driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(3) > button").send_keys(Keys.ENTER)
    oldcountC, newcountC = None, 0
    # 더보기 클릭
    while True:
        try:
            # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
            if oldcountC == newcountC:
                # print("old:", oldcountC, "new:", newcountC)
                break
            else:
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                oldcountC = len(reviews)
                # print("old:", oldcountC)
                btn = driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                newcountC = len(reviews)
                # print("new:", newcountC)
                # print()
        except:
            break

    driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(4) > button").send_keys(Keys.ENTER)
    oldcountD, newcountD = None, 0
    # 더보기 클릭
    while True:
        try:
            # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
            if oldcountD == newcountD:
                # print("old:", oldcountD, "new:", newcountD)
                break
            else:
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                oldcountD = len(reviews)
                # print("old:", oldcountD)
                btn = driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                newcountD = len(reviews)
                # print("new:", newcountD)
                # print()
        except:
            break
    driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(1) > button").send_keys(Keys.ENTER)
    oldcountA, newcountA = None, 0
    # 더보기 클릭
    while True:
        try:
            # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
            if oldcountA == newcountA:
                # print("old:", oldcountA, "new:", newcountA)
                break
            else:
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                oldcountA = len(reviews)
                # print("old:", oldcountA)
                btn = driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                newcountA = len(reviews)
                # print("new:", newcountA)
                # print()
        except:
            break
    time.sleep(2)
    i = 1
    comment_list = []
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > ul > li:nth-child("+str(i)+") > a").send_keys(Keys.ENTER) #댓글 클릭
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            comment = driver.find_element(By.CLASS_NAME,"ReviewCard__ReviewText").text
            comment = comment.replace('\n',"")
            comment_list.append(comment)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            i += 1
        except:
            # print(comment_list) #리스트에 댓글 다 쌓이고 브레이크 걸리기 전에 리스트 전체 보이는거
            break
    review_info = {"name": restaurantname, "count": [newcountA, newcountB, newcountC, newcountD]}
    review_list = {"name": restaurantname, "comment": comment_list}
    return [review_info, review_list]
