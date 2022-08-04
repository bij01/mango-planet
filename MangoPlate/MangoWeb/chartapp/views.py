from django.shortcuts import render
from pymongo import MongoClient


def connect_db():
    client = MongoClient(host='192.168.0.138', port=27017)
    db = client['restaurants']
    return db, client


def check_data(col):
    count = 0
    data_list = []
    for data in col.find().sort("_id"):
        for k, v in data.items():
            if k == "_id":
                pass
            else:
                count += 1
                # print(k, v)
                # data_list.append({k: v})
    return data_list, count
    # print(count)


def index(request):
    db, client = connect_db()
    col = db["info_list"]
    data_list, count = check_data(col)
    context = {
        'data_list': data_list,
        'count': count,
    }
    return render(request, "index.html", context)


def detail(request):
    context = {

    }
    return render(request, "detail.html", context)