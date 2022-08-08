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
        name = data.get("name")
        addr = data.get("info")[2]
        data_list.append({"name": name, "addr": addr})
        count += 1
    return data_list, count

def check_data2(col2):
    count2 = 0
    menu_list = []
    for data in col2.find().sort("_id"):
        name = data.get("name")
        menu = data.get("menu")
        if menu != {}:
            menu_list.append({"name":name, "menu":menu})
        else:
            menu_list.append({"name":name, "menu":"None"})
    #print(menu_list2)
    return menu_list, count2
    # print(count)

def index(request):
    db, client = connect_db()
    col = db["info_list"]
    col2 = db["menu_list"]
    info_list, count = check_data(col)
    menu_list, count2 = check_data2(col2)
    context = {
        'info_list': info_list,
        'menu_list': menu_list,
        'count': count,
        'count2': count2,
    }
    return render(request, "index.html", context)


def detail(request):
    db, client = connect_db()
    col = db["info_list"]
    col2 = db["menu_list"]
    info_list, count = check_data(col)
    menu_list, count2 = check_data2(col2)
    target_name = col.find({'name':'미영이네식당'})[0]
    target_menu = col2.find({'name':"미영이네식당"})[0]
    print(target_menu['menu'])
    target_menu1 = list(dict.keys(target_menu['menu']))
    target_price1 = list(dict.values(target_menu['menu']))
    #print(target_price1[0])
    context = {
        'target_name': target_name['name'],
        'target_star': target_name['info'][0],
        'target_veiw': target_name['info'][1],
        'target_addr': target_name['info'][2],
        'target_tel': target_name['info'][3],
        'target_price': target_name['info'][4],
        'target_menu': target_menu['menu'],
        }
    return render(request, "detail.html", context)



def favors(request):
    context = {
        
    }
    return render(request, "favors.html", context)