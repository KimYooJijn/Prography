from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required, PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from board.models import Board, BoardComment
from board.forms import BoardForm

# Create your views here.
def boardIndex(request):
    if request.method == 'GET':
        param = ''
        if request.GET.get('search'):
            data = Board.objects.filter(**{
                request.GET.get('search')+'__contains': request.GET.get('value')
            })
            param = request.get_full_path().split('?')[1]
        else:
            data = Board.objects.all()
        
        per_page = request.GET.get('per_page', 10)
        paginator = Paginator(data.order_by('-id'), per_page)
        page = paginator.page(request.GET.get('page', 1))
        
        context = {
            'data': page,
            'page_range': paginator.page_range,
            'per_page': per_page,
            'param': param,
        }

        response = render(request, 'board/index.html', context)
        response.set_cookie('per_page', per_page, max_age=60*60*24*7, path='/')
        return response

def boardView(request):
    if request.method == 'GET':
        data = Board.objects.get(id=request.GET.get('id'))
        comments = BoardComment.objects.filter(board_id=request.GET.get('id'))

        if not request.COOKIES.get('view_ids'):
            view_ids = f'{data.id}'
            data.view_cnt += 1
            data.save()
        else:
            view_ids = request.COOKIES.get('view_ids')
            if str(data.id) not in view_ids.split(','):
                data.view_cnt += 1
                data.save()
                view_ids = ','.join(set([view_ids, f'{data.id}']))

        context = {
            'data': data,
            'comments': comments
        }

        response = render(request, 'board/view.html', context)
        response.set_cookie('view_ids', view_ids, max_age=3600, path='/board/view/')
        return response


@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('board.add_board', raise_exception=True)
def boardAdd(request):
    if request.method == 'GET':
        form = BoardForm()
        context = {
            'form': form
        }
        return render(request, 'board/add.html', context)
    elif request.method == 'POST':
        data = Board.objects.create(
            title=request.POST.get('title'),
            username=request.user.username,
            b_type=request.POST.get('b_type'),
            content=request.POST.get('content')
        )
        
        upload_file = request.FILES['upload_file']
        if upload_file:
            data.upload_file = upload_file
            data.save()

        return redirect(f'{reverse("board:view")}?id={data.id}')


@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('board.change_board', raise_exception=True)
def boardMod(request):
    if request.method == 'GET':
        data = Board.objects.get(id=request.GET.get('id'))
        if data.username == request.user.username:
            form = BoardForm(initial={'content': data.content})
            context = {
                'data': data,
                'form': form,
            }
            return render(request, 'board/mod.html', context)
        else:
            raise PermissionDenied
    elif request.method == 'POST':
        data = Board.objects.get(id=request.POST.get('id'))
        if data.username == request.user.username:
            data.title = request.POST.get('title')
            data.content = request.POST.get('content')
            data.b_type = request.POST.get('b_type')
            data.save()

            return redirect(reverse('board:view')+f'?id={data.id}')
        else:
            raise PermissionDenied


@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('board.delete_board', raise_exception=True)
def boardDel(request):
    if request.method == 'GET':
        return render(request, 'board/del.html')


@login_required
def boardGood(request):
    if request.method == 'GET':
        return redirect('board:view')

@login_required
def boardBad(request):
    if request.method == 'GET':
        return redirect('board:view')


@require_POST
@login_required
def boardComment(request):
    if request.method == 'POST':
        data = BoardComment.objects.create(
            board_id=request.POST.get('board_id'),
            username=request.user.username,
            content=request.POST.get('content')
        )
        return redirect(reverse('board:view')+f'?id={data.board_id}')
