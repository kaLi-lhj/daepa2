from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from board.models import Board

# Create your views here.

def mainIndex(request):
    '''
    게시판 메인 페이지로써 모든 게시물에 대한
    정보를 출력 하기 위한 기능을 가진다.
    게시물 정보 -> id, title, author, view_cnt
    '''

    board = Board.objects.values(
        'id', 'title', 'sub_title', 'author', 'view_cnt').all().order_by('-id')
    data = {
        'board': board
    }
    return render(request, 'board/index.html', data)

def boardDetail(request, idx):
    '''
    게시판 세부 정보 페이지로써 idx에 해당하는
    게시물의 정보를 출력 한다.
    출력 정보 -> id, title, sub_titie, context, view_cnt
                like_cnt, hate_cnt, create_date, update_date
    '''
    try:
        board = Board.objects.get(id=idx)
        board.view_cnt = board.view_cnt + 1
        board.save(update_fields=('view_cnt',))
        data = {
            'board':board
        }
        return render(request, 'board/detail.html', data)
    except Board.DoesNotExist:
        return HttpResponse('해당 페이지가 존재하지 않습니다.')

def boardAdd(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            data = {
                'action':reverse('board:add'),
                'select_option':[('자유게시판', ), ('연예게시판', ), ('유머게시판', )]
            }
            return render(request, 'board/form.html', data)
        else:
            return redirect('login')
    elif request.method == 'POST':
        if request.user.is_authenticated():
            board = Board()
            board.title = request.POST.get('title')
            board.sub_title = request.POST.get('sub_title')
            board.author = request.user.username
            board.context = request.POST.get('context')
            board.no_del = request.POST.get('no_del', False)
            board.save()

            return redirect('board:detail', board.id)
        else:
            return redirect('login')

def boardUpdate(request, idx):
    if request.method == 'GET':
        try:
            board = Board.objects.get(id=idx)
            data = {
                'action':reverse('board:update', args=(idx,)),
                'select_option':[('자유게시판', ), ('연예게시판', ), ('유머게시판', )],
                'board':board
            }
            return render(request, 'board/form.html', data)
        except Board.DoesNotExist:
            return HttpResponse('해당 페이지가 존재하지 않습니다.')

    elif request.method == 'POST':
        board = Board.objects.get(id=idx)
        board.title = request.POST.get('title')
        board.sub_title = request.POST.get('sub_title')
        board.author = request.POST.get('author')
        board.context = request.POST.get('context')
        board.no_del = request.POST.get('no_del', False)
        board.save(update_fields=('title', 'sub_title', 'author',
            'context', 'no_del', 'update_date'))
        return redirect('board:detail', idx)

def boardDelete(request, idx):
    if Board.objects.values('no_del').get(id=idx)['no_del'] :
        # return HttpResponse('삭제 금지 게시판 입니다. (삭제 불가)')
        return redirect('err:message', 'nodel')
                        # '/error/nodel/'
    else:
        Board.objects.get(id=idx).delete()
    return redirect('board:index')

def boardLikeHate(request):
    if request.user.is_authenticated():
        idx = int(request.GET.get('bid'))
        board = Board.objects.get(id=idx)
        if request.GET.get('like') == 'True':
            board.like_cnt = board.like_cnt + 1
        else:
            board.hate_cnt = board.hate_cnt + 1
        board.view_cnt = board.view_cnt - 1
        board.save(update_fields=('like_cnt', 'hate_cnt', 'view_cnt'))

        return redirect('board:detail', idx)
    else:
        return redirect('err:message', 'noAuth')