from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def collect_review(driver, url):
    # 지예성
    print("test start")
    driver.get(url)
    driver.implicitly_wait(30)
    name = driver.find_element(By.CLASS_NAME, "restaurant_name").text
    # print(restaurantname)

    # 전체(1), 맛있다(2), 괜찮다(3), 별로(4)
    def css_url(num):
        selector = f"body > main > article > div.column-wrapper > div.column-contents > div " \
              f"> section.RestaurantReviewList > header > ul > li:nth-child({num}) > button"
        return selector

    review_count = []
    # 리뷰 카운트(전체, 맛있다, 괜찮다, 별로)
    counts = driver.find_elements(By.CLASS_NAME, 'RestaurantReviewList__ReviewCount')
    for count in counts:
        review_count.append(count.text)

    # 리뷰 카운트 리턴
    def count_review(num):
        oldcount, newcount = -1, 0
        if int(review_count[int(num)-1]) == 0:
            return newcount
        else:
            # 댓글 세부창 클릭
            driver.find_element(By.CSS_SELECTOR, css_url(num)).send_keys(Keys.ENTER)
            # 더보기 클릭
            while True:
                try:
                    # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
                    if oldcount == newcount:
                        break
                    else:
                        reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                        oldcount = len(reviews)
                        btn = driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(1)
                        reviews = driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                        newcount = len(reviews)
                except:
                    break
            return newcount

    good = count_review("2")
    soso = count_review("3")
    notgood = count_review("4")
    total = count_review("1")

    review_info = {"name": name, "count": [total, good, soso, notgood]}
    # 전체 리뷰 수집
    i = 1
    comment_list = []
    while True:
        try:
            reply_button = driver.find_element(By.CSS_SELECTOR,
                                               "body > main > article > div.column-wrapper > div.column-contents > div "
                                               "> section.RestaurantReviewList > ul > li:nth-child("+str(i)+") > a")
            reply_button.send_keys(Keys.ENTER)  # 댓글 클릭
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            comment = driver.find_element(By.CLASS_NAME, "ReviewCard__ReviewText").text
            comment = comment.replace('\n', "")
            comment_list.append(comment)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            i += 1
        except:
            break

    review_list = {"name": name, "comment": comment_list}
    return [review_info, review_list]


def test():
    path = "c:/python/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(3)
    url = "https://www.mangoplate.com/top_lists"
    driver.get(url)
    test_url = "https://www.mangoplate.com/restaurants/23yYn1YCt-HR"
    rinfo, rlist = collect_review(driver, test_url)
    print(rinfo)


# test()
