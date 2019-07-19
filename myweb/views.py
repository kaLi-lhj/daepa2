from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from random import random
from django.contrib.auth import logout

def mainIndex(request):
    data = {
        'link':{
            random()*10:('게시판', reverse('board:index')),
            random()*20:('뉴스', reverse('news:index')),
            random()*30:('웹툰', reverse('webtoon:index')),
            random()*40:('사전', reverse('dict:index')),
            
        }
    }
    return render(request, 'index.html', data)

def regAccount(request):
    if request.method == 'GET':
        data = {
            'action':reverse('reg_account'),
            'type':'가입'
        }
        return render(request, 'registration/register.html', data)
    elif request.method == 'POST':
        # 동일한 계정이 있는지 체크
        if User.objects.filter(username=request.POST.get('username')).exists():
            # 동일한 계정이 있음을 알려줌
            data = {
                'username_info': True,
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
            }
            return render(request, 'registration/register.html', data)
        else:
            # 2개의 패스워드가 일치하는지 체크
            if request.POST.get('password') == request.POST.get('chkpw'):
                # 계정 생성
                user = User()
                user.username = request.POST.get('username')
                user.set_password(request.POST.get('password'))
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                user.save()

                return redirect('login')
            else:
                data = {
                    'password_info': True,
                    'username': request.POST.get('username'),
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'email': request.POST.get('email'),
                }
                return render(request, 'registration/register.html', data)


def modiAccount(request):
    # 회원 정보 수정
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        data = {
            'action': reverse('modi_account'),
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'type':'수정'
        }
        return render(request, 'registration/register.html', data)
    elif request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        return redirect('login')








