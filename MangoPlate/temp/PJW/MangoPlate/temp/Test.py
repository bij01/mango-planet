# import threading
# import time
#
# def run(x, y):
#     for i in range(x, y):
#         time.sleep(1)
#         print(i)
#
#
# goal_num = 301
# goal_list = [0]
# for x in range(5):
#     if x == 0:
#         pass
#     else:
#         st_num = goal_num / x / x
#         # print(st_num)
#         goal_list.append(round(st_num) * x)
#         goal_list.sort()
# # print(goal_list)
# for x in range(5-1):
#     print(goal_list[x], goal_list[x+1])
# th_list = []
# for x in range(5-1):
#     th = threading.Thread(target=run, args=(goal_list[x], goal_list[x+1]), daemon=True)
#     th_list.append(th)
# print(th_list)
#
# th_list[0].start()
# th_list[1].start()
# th_list[2].start()
# th_list[3].start()
#
# th_list[0].join()
# th_list[1].join()
# th_list[2].join()
# th_list[3].join()

# f = open(r"C:\Users\User\Desktop\log2.txt", "rt", encoding='utf-8')
# rlist = f.readlines()
# nlist = []
# for r in rlist:
#     x = r[r.index(" ", 15):]
#
#
# nlist.sort()
# print(nlist)

st = 0
ed = 1000

target_list = []
tlist = []
end_num = ed
num = round((end_num-st) / 6)

for x in range(0, 6):
    addnum = (st + round(num) * x)
    target_list.append(addnum)
target_list.append(end_num+1)
target_list.sort()

print(target_list)

# import datetime
# import time
#
# start_time = 1655665638.7538123
# start_time2 = 1658668812.1204917
# end_time = time.time()
# run_time = datetime.timedelta(seconds=end_time - start_time2)
#
# run_time = str(run_time).split(",")
# if len(run_time) == 2:
#     day = run_time[0].replace(" days", "")
#     clock = run_time[1].strip()
#     if len(clock) == 15:
#         hour = clock[0:2]
#         mins = clock[3:5]
#         secs = clock[6:8]
#         print(f"작동시간: {day}일 {hour}시간 {mins}분 {secs}초")
#     else:
#         hour = clock[0:1]
#         mins = clock[2:4]
#         secs = clock[5:7]
#         print(f"작동시간: {day}일 {hour}시간 {mins}분 {secs}초")
# else:
#     clock = run_time[0].strip()
#     if len(clock) == 15:
#         hour = clock[0:2]
#         mins = clock[3:5]
#         secs = clock[6:8]
#         print(f"작동시간: {hour}시간 {mins}분 {secs}초")
#     else:
#         hour = clock[0:1]
#         mins = clock[2:4]
#         secs = clock[5:7]
#         print(f"작동시간: {hour}시간 {mins}분 {secs}초")