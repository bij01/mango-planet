from sqlite3 import connect
from django.shortcuts import render
from pymongo import MongoClient

def connect_db():
    client = MongoClient(host='192.168.0.138', port=27017)
    db = client['restaurants']
    return db, client

def check_data1(col):
    count = 0
    data_list = []
    for data in col.find().sort("_id"):
        for k, v in data.items():
            if k == "_id":
                pass
            else:
                count += 1
                # print(k, v)
                data_list.append({k: v})
    return data_list, count
    # print(count)
    
def check_data2(col6,col7):
    db, client = connect_db()
    col6 = db["review_info_list"]
    col7 = db["location_info"]
    count = 0
    data_list = []
    review_rate = []
    for data in col7.find().limit(10):
        name = data.get("name")
        addr_x = data.get("loc")["X"]
        addr_y = data.get('loc')["Y"]
        data_list.append({"name":name, "X":addr_x, "Y":addr_y})
    #print(data_list)
    for data in col6.find().limit(10):
        name = data.get("name")
        g_1 = data.get("count")[1]
        g_2 = data.get("count")[2]
        g_3 = data.get("count")[3]
        review_rate.append({"name":name, "G":g_1, "S":g_2, "B":g_3})
    #print(review_rate[0]["G"])
    return data_list, count, review_rate
    # print(count)


def index(request):
    db, client = connect_db()
    col = db["info_list"]
    data_list, count = check_data1(col)
    for data in col.find():
        name = data.get
    context = {
       'data_list': data_list,
       'count': count,
    }
    return render(request, "index.html", context)


def detail(request):
    context = {

    }
    return render(request, "detail.html", context)


def favors(request):
    context = {
        
    }
    return render(request, "favors.html", context)

def Test(request):
    db, client = connect_db()
    col6 = db["review_info_list"]
    col7 = db["location_list"]
    data_list, count, review_rate = check_data2(col6, col7)
    context = {
        'data_list1': data_list[0]["Y"],
        'data_list2': data_list[0]["X"],
        'review_rate1': review_rate[2]["G"],
        'review_rate2': review_rate[2]["S"],
        'review_rate3': review_rate[2]["B"],
        'res_name': data_list[0]["name"],
    }
    return render(request, 'Test.html', context)
