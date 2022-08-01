from django.shortcuts import render
from pymongo import MongoClient


def connect_db():
    client = MongoClient(host='192.168.0.138', port=27017)
    db = client['restaurants']
    return db, client


def check_data(col):
    count = 0
    for data in col.find():
        for k, v in data.items():
            if k == "_id":
                pass
            else:
                count += 1
                # print(k, v)
    # print(count)


def index(request):
    db, client = connect_db()
    col = db["link_list"]
    check_data(col)
    context = {

    }
    return render(request, "index.html", context)
