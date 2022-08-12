from django.shortcuts import render
from pymongo import MongoClient
from django.core.paginator import Paginator


def connect_db():
    client = MongoClient(host='192.168.0.138', port=27017)
    db = client['restaurants']
    return db, client


def check_data(col, key, *args):
    count = 0
    data_list = []
    if key == "":
        for data in col.find().sort("_id"):
            name = data.get("name")
            addr = data.get("info")[2]
            count += 1
            data_list.append([name,addr])
    else:
        for data in col.find({"name": {"$regex": key}}).sort("_id"):
            name = data.get("name")
            addr = data.get("info")[2]
            count += 1
            data_list.append([name, addr])
        for data in col.find({"info": {"$regex": key}}).sort("_id"):
            name = data.get("name")
            addr = data.get("info")[2]
            count += 1
            data_list.append([name, addr])
    return data_list, count


def check_data1(col2):
    count2 = 0
    menu_list = []
    for data in col2.find().sort("_id"):
        name = data.get("name")
        menu = data.get("menu")
        if menu != {}:
            menu_list.append({"name": name, "menu": menu})
        else:
            menu_list.append({"name": name, "menu": "None"})
    return menu_list, count2


def check_data2(res_name):
    db, client = connect_db()
    col6 = db["review_info_list"]
    col7 = db["location_info"]
    try:
        data1 = col6.find_one({"name": res_name})
        name = data1["name"]
        g_1 = data1["count"][1]
        g_2 = data1["count"][2]
        g_3 = data1["count"][3]
        review_rate = {"name": name, "G": g_1, "S": g_2, "B": g_3}
    except:
        review_rate = {"name": res_name, "G": 0, "S": 0, "B": 0}
    try:
        data = col7.find_one({"name": res_name})
        name = data.get("name")
        addr_x = data.get("loc")["X"]
        addr_y = data.get('loc')["Y"]
        location = {"name": name, "X": addr_x, "Y": addr_y}
    except:
        location = {"name": res_name, "X": 0, "Y": 0}

    return location, review_rate


def index(request):
    key = request.GET.get("key")
    page = request.GET.get('page')  # 페이지
    # print(key, page)
    if key is None:
        key = ""
    db, client = connect_db()
    col = db["info_list"]
    col2 = db["menu_list"]
    info_list, count = check_data(col, key, col2)
    menu_list, count2 = check_data1(col2)

    paginator = Paginator(info_list, 12)  # 페이지당 12개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'menu_list': menu_list,
        'count': count,
        'count2': count2,
        'data_list': page_obj,
        'key': key,
    }
    return render(request, "index.html", context)


def detail(request, name):
    db, client = connect_db()

    # 즐겨찾기 추가
    email = request.session.get("email")
    favor_list = []
    if email is None:
        pass
    else:
        res_name = request.GET.get("res_name")
        col = db["favor_list"]
        if res_name is not None:
            request.session["res_name"] = res_name
            req_len = len(res_name.split("-"))
            res_name = res_name.split("-")[0]
            # 즐겨찾기 클릭 했을 경우
            if req_len == 1:
                favor = col.find_one({"email": email})
                # DB에 해당 유저의 즐겨찾기 목록이 비어 있지 않을 경우
                if favor is not None:
                    print("db 업데이트")
                    print(favor["list"])
                    if res_name is not None:
                        try:
                            favor["list"].remove(res_name)
                        except:
                            pass
                    favor_list += favor["list"]
                    favor_list.append(res_name)
                    col.update_one(filter={"email": email}, update={"$set": {"list": favor_list}})
                # DB에 해당 유저의 즐겨찾기 목록이 비어 있을 경우
                else:
                    print("db 추가")
                    favor_list.append(res_name)
                    col.insert_one({"email": email, "list": favor_list})
            # 즐겨찾기 해제 했을 경우
            else:
                # print("db 제거")
                favor = col.find_one({"email": email})
                favor_list = favor["list"]
                # print("res_name", res_name)
                try:
                    favor["list"].remove(res_name)
                except:
                    pass
                # print(favor_list)
                col.update_one(filter={"email": email}, update={"$set": {"list": favor_list}})
            # END
        # 즐겨찾기 목록 불러오기
        favor = col.find_one({"email": email})
        if favor is not None:
            favor_list += favor["list"]
    res_name = name
    # 댓글 TOP5 차트
    review_col = db["review_chart"]
    data = review_col.find_one({"name": res_name})
    if data is not None:
        x_list = data["x_list"]
        y_list = data["y_list"]
    else:
        x_list = []
        y_list = []
    # TOP5 END
    col1 = db["info_list"]
    col2 = db["menu_list"]
    location, review_rate = check_data2(res_name)
    target = col1.find({'name': res_name})[0]
    menu_list = col2.find_one({"name": res_name})["menu"]

    context = {
        'data_list1': location["Y"],
        'data_list2': location["X"],
        'review_rate1': review_rate["G"],
        'review_rate2': review_rate["S"],
        'review_rate3': review_rate["B"],
        'name': target['name'],
        'star': target['info'][0],
        'view': target['info'][1],
        'addr': target['info'][2],
        'tel': target['info'][3],
        'price': target['info'][4],
        'menu_list': menu_list,
        'favor_list': favor_list,
        'x_list': x_list,
        'y_list': y_list,
    }
    return render(request, "detail.html", context)


def favors(request):
    page = request.GET.get('page')  # 페이지
    db, client = connect_db()
    col = db["info_list"]
    col2 = db["menu_list"]
    col3 = db["favor_list"]

    data_list = []
    count = 0
    menu_list = []
    count2 = 0
    email = request.session.get("email")
    if email is None:
        pass
    else:
        datafav = col3.find_one({"email": email})
        if datafav is None:
            pass
        else:
            namelist = datafav.get("list")
            for name in namelist:
                for data in col.find({"name": name}).sort("_id"):
                    name = data.get("name")
                    addr = data.get("info")[2]
                    count += 1
                    data_list.append([name, addr])
            menu_list, count2 = check_data1(col2)

    paginator = Paginator(data_list, 12)  # 페이지당 12개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'menu_list': menu_list,
        'count': count,
        'count2': count2,
        'data_list': page_obj,
    }
    return render(request, "favors.html", context)

def guide(request):

    return render(request, "guide.html")
