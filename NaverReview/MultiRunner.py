import threading
from ReviewCollector import ReviewCollector
import time


# 시작번호, 끝번호, 모드 설정(2 == 식당목록, 그외 == 식당정보, 리뷰)
def run(start, end, mode):
    x = ReviewCollector(start, end, mode=mode)
    x.close_db()
    x.driver.close()
    print(f"DB & WebDriver Closed {start}/{end}")


def first_run():
    # 테마별 식당 리스트 링크 수집
    firstrun = ReviewCollector(None, None, None)
    firstrun.collect_theme_list()
    firstrun.close_db()
    firstrun.driver.close()


start_time = time.time()


# first_run()  # 테마별로 분류된 링크 수집(처음 한번만 실행)
# 식당 목록 또는 식당 정보와 리뷰 수집
def run_thread(*args):
    # 모드(2, else), 쓰레드를 나눌 수, 시작 번호, 끝 번호
    target_list = [args[2]]
    tlist = []
    end_num = args[3]
    for x in range(args[1]):
        if x == 0:
            pass
        else:
            num = end_num / x / x
            target_list.append(round(num) * x)
    target_list.sort()
    for x in range(args[1]-1):
        th = threading.Thread(target=run, args=(target_list[x], target_list[x+1], args[0]), daemon=True)
        tlist.append(th)
    if args[1] == 6:
        tlist[0].start()
        tlist[1].start()
        tlist[2].start()
        tlist[3].start()
        tlist[4].start()
        tlist[0].join()
        tlist[1].join()
        tlist[2].join()
        tlist[3].join()
        tlist[4].join()
    elif args[1] == 4:
        tlist[0].start()
        tlist[1].start()
        tlist[2].start()
        tlist[0].join()
        tlist[1].join()
        tlist[2].join()
    else:
        pass


run_thread(3, 6, 0, 100)  # 모드, 쓰레드를 나눌 수(6-> 5쓰레드, 4-> 3쓰레드), 시작 번호, 끝 번호

end_time = time.time()
run_time = time.localtime(end_time - start_time)
print(f"걸린시간: {run_time.tm_hour}시 {run_time.tm_min}분 {run_time.tm_sec}초")
