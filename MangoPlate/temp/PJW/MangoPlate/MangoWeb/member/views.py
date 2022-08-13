from re import template
from unittest import result
from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from member.models import Member
from .forms import RegisterForm
from django.contrib import auth
from django.template import loader


def login(request):
    return render(request, "login.html")

def login_ok(request):
    # email = request.POST['email'] #방법1
    # pwd = request.POST['pwd'] #방법1   
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print("email", email, "pwd", pwd)
    
    try:
        member = Member.objects.get(email=email)
        print("member", member)
    except Member.DoesNotExist:
        member = None
    
    result = 0
    if member != None:
        print("해당 email회원 존재함")
        if member.pwd == pwd:
            print("비밀번호까지 일치")
            result = 2
            request.session['email'] = email #방법2
            request.session['name'] = member.name
        else:
            print("비밀번호 틀림")
            result = 1
    else:
        print("해당 email회원이 존재하지 않음")
        result = 0
    template = loader.get_template("login_ok.html")
    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('email'):
        print("로그아웃성공")
        del request.session['email']
        request.session.flush()
        print("세션삭제성공")
    return redirect("/")

    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            pwd2 = request.POST["password2"]
            if pwd == pwd2:
                name = request.POST.get('name')
                email = request.POST.get('email')
                pwd = request.POST.get('pwd')
                
                if Member.objects.filter(email=request.POST['email']).exists():  
                    print("이메일중복")
                    message = "1"
                    context = {
                        "msg": message,
                    }
                
                    return render(request, "register.html", context)
                else:
                    user = Member(name=name, email=email, pwd=pwd, rdate=DateTime)
                    user.save()
                    # 여기 추가함
                    request.session['email'] = email
                    request.session['name'] = name
                    
                    return render(request, "register_ok.html")
                # try:
                #     Member.objects.get(primarykey=email)
                #     print('email', '이미 가입된 이메일입니다.')
                # except:
                #     pass  
            
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

def register_ok(request):
    return render(request, "register_ok.html")
