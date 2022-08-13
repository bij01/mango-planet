from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from member.models import Member, Qna
from .forms import RegisterForm
from django.template import loader
from django.contrib import messages


def login(request):
    # email = request.POST['email'] #방법1
    # pwd = request.POST['pwd'] #방법1
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print("email", email, "pwd", pwd)

    if email is None and pwd is None:
        result = -1
    else:
        try:
            member = Member.objects.get(email=email)
            print("member", member)
        except Member.DoesNotExist:
            member = None
        if member is not None:
            print("email회원 존재")
            if member.pwd == pwd:
                print("비밀번호 일치")
                result = 2
                request.session['email'] = email
                request.session['name'] = member.name
                return redirect('chart:index')
            else:
                print("비밀번호 틀림")
                messages.error(request, "비밀번호가 일치하지 않습니다.")
                result = 1
        else:
            print("해당 email회원이 존재하지 않음")
            messages.error(request, "해당 email로 등록된 계정이 없습니다.")
            result = 0

    context = {
        'result': result,
    }
    return render(request, "login.html", context)


def logout(request):
    if request.session.get('email'):
        print("로그아웃성공")
        del request.session['email']
        request.session.flush()
        print("세션삭제성공")
    return redirect("/")

    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
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
                    # print("이메일 중복")
                    messages.error(request, "중복된 이메일 입니다.")
                    return redirect('member:register')
                else:
                    user = Member(name=name, email=email, pwd=pwd, rdate=DateTime)
                    user.save()
                    request.session['email'] = email
                    request.session['name'] = name
                    return render(request, "register_ok.html")
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')
                return redirect('member:register')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def register_ok(request):
    return render(request, "register_ok.html")


def opinion(request):
    if request.method == "POST":
        writer = request.POST.get('email')
        comment = request.POST.get('comment')
        opinion = Qna(writer=writer, comment=comment, rdate=DateTime)
        opinion.save()
        request.session['writer'] = writer
        request.session['comment'] = comment
        
        return render(request, "opinion_ok.html")
    else:
        return render(request, "opinion.html")
    
    
def opinion_ok(request):
    return render(request, "opinion_ok.html")

        
        
    