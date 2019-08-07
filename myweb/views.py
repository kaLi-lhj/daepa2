from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from random import random
from django.contrib.auth import logout
from myweb.models import Profile

def main(request):
    return render(request, 'main/index.html')

def mainIndex(request):
    data = {
        'link':{
            random()*10:('게시판', reverse('board:index')),
            random()*20:('뉴스', reverse('news:index')),
            random()*30:('웹툰', reverse('webtoon:index')),
            random()*40:('공고', reverse('gonggo:index')),
            
        }
    }
    return render(request, 'index.html', data)

def regAccount(request):
    return render(request,'registration/register.html')



def join1(request):
    if request.method == 'GET':
        data = {
            'action':reverse('join1'),
            'type':'가입'
        }
        return render(request, 'registration/join1.html', data)
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
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["chkpw"])
                #회원가입 받아오기
                name = request.POST["name"]
                job = request.POST["job"]
                address = request.POST["address"]
                email = request.POST["email"]
                phone_num = request.POST["phone_num"]
                gender = request.POST["gender"]
                date_of_birth = request.POST["date_of_birth"]
                interest = request.POST.get("interest",'False')
                
                profile = Profile(user=user, name=name, job=job, address=address, email=email, phone_num=phone_num, gender=gender, date_of_birth=date_of_birth, interest = interest)
                profile.save()
               
                return redirect('login')
            else:
                data = {
                    'password_info': True,
                    'job': request.POST.get('employee'),
                    'username': request.POST.get('username'),
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'email': request.POST.get('email'),
                }
                return render(request, 'registration/join1.html', data)

def join2(request):
    if request.method == 'GET':
        data = {
            'action':reverse('join2'),
            'type':'가입'
        }
        return render(request, 'registration/join2.html', data)
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
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["chkpw"])
                #회원가입 받아오기
                name = request.POST["name"]
                job = request.POST["job"]
                address = request.POST["address"]
                email = request.POST["email"]
                phone_num = request.POST["phone_num"]
                
                
                company=request.POST['company']
                profile = Profile(user=user, name=name, job=job, address=address, email=email, phone_num=phone_num, company=company)
                profile.save()
               
                return redirect('login')
            else:
                data = {
                    'password_info': True,
                    'job': request.POST.get('employee'),
                    'username': request.POST.get('username'),
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'email': request.POST.get('email'),
                }
                return render(request, 'registration/join2.html', data)

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
            'type':'정보 수정'
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

def modi(request):
    # 회원 정보 수정
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        data = {
            'action': reverse('modi'),
            'username': user.username,
            'name': user.profile.name,
            'job' : user.profile.job,
            'address' : user.profile.address,
            'email': user.profile.email,
            'phone_num' : user.profile.phone_num,
            'gender' : user.profile.gender,
            'date_of_birth' : user.profile.date_of_birth,
            'company' : user.profile.company,
            'interest' : user.profile.interest
        }
        return render(request, 'modi/index.html', data)
    elif request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.profile.name = request.POST["name"]
        user.profile.job = request.POST["job"]
        user.profile.address = request.POST["address"]
        user.profile.email = request.POST["email"]
        user.profile.phone_num = request.POST["phone_num"]
        
        if user.profile.job == "employee":
            user.profile.gender = request.POST["gender"]
            user.profile.date_of_birth = request.POST["date_of_birth"]
            user.profile.interest = request.POST["interest"]
        else:
            user.profile.company = request.POST["company"]
        
        user.profile.save()
        
        return redirect('main')








