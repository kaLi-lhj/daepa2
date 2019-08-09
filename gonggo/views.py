from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from gonggo.models import Gonggo

# Create your views here.
def mainIndex(request):
    # data = Gonggo.objects.get(id=1)
    data = Gonggo.objects.all()

    return render(request, 'gonggo/index.html',{"gonggo":data})

def gonggoForm(request):
    if request.method == 'GET':
        data = {
            'action':reverse('gonggo:add'),
            
        }
        return render(request, 'gonggo/form.html', data)
        
    elif request.method == 'POST':
    
        gonggo = Gonggo()
        gonggo.title = request.POST.get('title')
        gonggo.interest = request.POST.get('interest')
        gonggo.workDetail=request.POST.get('workDetail')
        gonggo.serviceAddr2=request.POST.get('serviceAddr2')
        gonggo.salary=request.POST.get('salary')
        gonggo.minMoney=request.POST.get('minMoney')
        gonggo.highMoney=request.POST.get('highMoney')
        gonggo.workTimeDetailContent=request.POST.get('workTimeDetailContent')
        gonggo.manager1=request.POST.get('manager1')
        gonggo.phonenum=request.POST.get('phonenum')
        gonggo.email=request.POST.get('email')
        gonggo.save()

        return redirect('gonggo:detail', gonggo.id)
        
def gonggoDetail(request, idx):
    '''
    게시판 세부 정보 페이지로써 idx에 해당하는
    게시물의 정보를 출력 한다.
    출력 정보 -> id, title, sub_titie, context, view_cnt
                like_cnt, hate_cnt, create_date, update_date
    '''
    try:
        gonggo = Gonggo.objects.get(id=idx)
        
        data = {
            'gonggo':gonggo
        }
        return render(request, 'gonggo/detail.html', data)
    except Gonggo.DoesNotExist:
        return HttpResponse('해당 페이지가 존재하지 않습니다.')


def gonggoAdd(request):
    if request.method == 'GET':
    
        data = {
            'action':reverse('gonggo:add'),
            
        }
        return render(request, 'gonggo/form.html', data)
    
    elif request.method == 'POST':
        gonggo = Gonggo()
        gonggo.title = request.POST['title']
        gonggo.interest = request.POST['interest']
        gonggo.workDetail=request.POST['workDetail']
        gonggo.serviceAddr2=request.POST['serviceAddr2']
        gonggo.salary=request.POST['salary']
        gonggo.minMoney=request.POST['minMoney']
        gonggo.highMoney=request.POST['highMoney']
        gonggo.workTimeDetailContent=request.POST['workTimeDetailContent']
        gonggo.manager1=request.POST['manager1']
        gonggo.phonenum=request.POST['phonenum']
        gonggo.email=request.POST['email']
        gonggo.save()
        
        return redirect('gonggo:detail', gonggo.id)
        
def gonggoUpdate(request, idx):
    if request.method == 'GET':
        try:
            gonggo = Gonggo.objects.get(id=idx)
            data = {
                'action':reverse('gonggo:update', args=(idx,)),
                'gonggo':gonggo
            }
            return render(request, 'gonggo/form.html', data)
        except Gonggo.DoesNotExist:
            return HttpResponse('해당 페이지가 존재하지 않습니다.')

    elif request.method == 'POST':
        gonggo = Gonggo.objects.get(id=idx)
        gonggo.title = request.POST['title']
        gonggo.interest = request.POST['interest']
        gonggo.workDetail=request.POST['workDetail']
        gonggo.serviceAddr2=request.POST['serviceAddr2']
        gonggo.salary=request.POST['salary']
        gonggo.minMoney=request.POST['minMoney']
        gonggo.highMoney=request.POST['highMoney']
        gonggo.workTimeDetailContent=request.POST['workTimeDetailContent']
        gonggo.manager1=request.POST['manager1']
        gonggo.phonenum=request.POST['phonenum']
        gonggo.email=request.POST['email']
        gonggo.save(update_fields=('title', 'interest', 'workDetail',
            'serviceAddr2', 'salary', 'minMoney', 'highMoney', 'workTimeDetailContent'
            ,'manager1','phonenum','email'))
        return redirect('gonggo:detail', idx)

def gonggoDelete(request, idx):
    
    Board.objects.get(id=idx).delete()
    return redirect('board:index')
