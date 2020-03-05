from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def webtoonWeek(request, week):
    week_map = {'mon': '월요', 'tue': '화요', 'wed': '수요',
    'thu': '목요', 'fri': '금요', 'sat': '토요', 'sun': '일요'}

    message = f'<h1>{week_map.get(week)} 웹툰 입니다.</h1>'
    
    return HttpResponse(message)

def webtoonYear(request, year):
    return render(request, 'index.html')

def newsDate(request, year, month, day):
    message = f'<h1>{year}년 {month}월 {day}일자 뉴스 입니다.</h1>'
    return HttpResponse(message)

def userJoin(request):
    if request.method == 'GET':
        return render(request, 'registration/join.html')
    elif request.method == 'POST':
        if request.POST.get('password') == request.POST.get('pass_chk'):
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
            )
            return redirect('/')
        else:
            context = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'error': 'password_error',
                'message': '패스워드를 다시 확인하세요.'
            }
            return render(request, 'registration/join.html', context)


@login_required
def userInfo(request):
    if request.method == 'GET':
        return render(request, 'registration/userinfo.html')
    elif request.method == 'POST':
        auth = authenticate(username=request.user.username, password=request.POST.get('password'))
        if auth:
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            return redirect('userinfo')
        else:
            context = {
                'error': 'password_error',
                'message': '패스워드를 다시 확인하세요.'
            }
            return render(request, 'registration/userinfo.html', context)