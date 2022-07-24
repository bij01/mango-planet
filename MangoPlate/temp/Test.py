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

f = open(r"C:\Users\User\Desktop\log2.txt", "rt", encoding='utf-8')
rlist = f.readlines()
nlist = []
for r in rlist:
    x = r[r.index(" ", 15):]


nlist.sort()
print(nlist)




