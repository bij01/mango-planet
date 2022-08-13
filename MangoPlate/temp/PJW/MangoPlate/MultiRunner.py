import threading
from MainCollector import MainCollector
import time
import datetime


# 시작번호, 끝번호, 모드 설정(2 == 식당목록, 그외 == 식당정보, 리뷰)
def run(mode, start, end):
    x = MainCollector(mode, start, end)
    x.close_db()
    x.driver.close()
    print(f"DB & WebDriver Closed start:{start} end:{x.get_current_page()+1} goal:{end}")


# 테마별 식당 리스트 링크 수집
def first_run():
    firstrun = MainCollector(None, None, None)
    firstrun.collect_theme_list()
    firstrun.close_db()
    firstrun.driver.close()


start_time = time.time()


# 식당 목록 또는 식당 정보와 리뷰 수집
def run_thread(*args):
    # 모드(2, else), 쓰레드를 나눌 수, 시작 번호, 끝 번호
    target_list = []
    tlist = []
    start_num = args[2]
    end_num = args[3]
    num = round((end_num - start_num) / args[1])
    for x in range(0, args[1]):
        addnum = (start_num + round(num) * x)
        target_list.append(addnum)
    target_list.append(end_num+1)
    target_list.sort()
    print(f"탐색범위: {target_list}")
    for x in range(args[1]):
        th = threading.Thread(target=run, args=(args[0], target_list[x], target_list[x+1]), daemon=True)
        tlist.append(th)
    if args[1] == 5:
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


# 프로그램 작동 시간 출력
def show_runtime():
    run_time = datetime.timedelta(seconds=end_time - start_time)

    run_time = str(run_time).split(",")
    if len(run_time) == 2:
        day = run_time[0].replace(" days", "")
        clock = run_time[1].strip()
        if len(clock) == 15:
            hour = clock[0:2]
            mins = clock[3:5]
            secs = clock[6:8]
            print(f"작동시간: {day}일 {hour}시간 {mins}분 {secs}초")
        else:
            hour = clock[0:1]
            mins = clock[2:4]
            secs = clock[5:7]
            print(f"작동시간: {day}일 {hour}시간 {mins}분 {secs}초")
    else:
        clock = run_time[0].strip()
        if len(clock) == 15:
            hour = clock[0:2]
            mins = clock[3:5]
            secs = clock[6:8]
            print(f"작동시간: {hour}시간 {mins}분 {secs}초")
        else:
            hour = clock[0:1]
            mins = clock[2:4]
            secs = clock[5:7]
            print(f"작동시간: {hour}시간 {mins}분 {secs}초")

# first_run()  # 테마별로 분류된 링크 수집(처음 한번만 실행)


# 프로그램 설정
run_thread(3, 5, 0, 1000)  # 모드, 쓰레드를 나눌 수, 시작 번호, 끝 번호

# 프로그램 작동 시간 출력
end_time = time.time()
show_runtime()
