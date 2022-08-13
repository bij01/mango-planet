# from MangoPlate.DataManager import DataManager as dm
#
# col1, col2, col3, col4, col5, col6 = dm.connect_db(dm())
# col = col3
# start_num = 500
# end_num = 510
# x = 0  # 현재 페이지
# count = 0  # 전체 페이지
#
# for _ in col.find():
#     count += 1
# print(count)
# for data in col.find():
#     for key, value in data.items():
#         if key == "_id":
#             pass
#         else:
#             if x not in range(start_num, end_num):
#                 # print("pass", x)
#                 pass
#             else:
#                 print(x)
#             if col == col2:
#                 # 식당 목록 중에 지정된 범위내 에서만 데이터 수집
#                 if x not in range(start_num, end_num):
#                     # print("pass", x)
#                     pass
#                 else:
#                     print(f"식당 정보 & 리뷰 크롤링 중.. {x}/{count}")
#                     # info_dict, menu_dict = collect_infomation(driver, value)
#                     for k, v in info_dict.items():
#                         if k in dm.check_data2(dm(), col3):
#                             print(f"중복 데이터 패스 {x}, {info_dict}")
#                             pass
#                         else:
#                             pass
#                             # dm.insert_data(dm(), col3, info_dict)
#                             # dm.insert_data(dm(), col4, menu_dict)
#                         # info, review = collect_review(driver, value)
#                     for k, v in info.items():
#                         if k in dm.check_data2(dm(), col5):
#                             print(f"중복 데이터 패스 {x}, {info}")
#                             pass
#                         else:
#                             pass
#                             # dm.insert_data(dm(), col5, info)
#                             # dm.insert_data(dm(), col6, review)
#             else:
#                 pass
#             x += 1
link_list = {}

link_list["title"] = "타이틀"
link_list["link"] = "http:///asdfklasjkldf"


