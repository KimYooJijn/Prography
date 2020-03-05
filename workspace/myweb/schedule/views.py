from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from schedule.models import Schdule

@require_GET
@login_required
@permission_required('schedule.view_schdule', raise_exception=True)
def scheduleIndex(request):
    # if any(request.GET):
    #     where = {
    #         'flag': request.GET.get('flag'),
    #         request.GET.get('s_type'): request.GET.get('s_value')
    #     }
    #     data = Schdule.objects.filter(**where)
    # else:
    #     data = Schdule.objects.all()

    data = Schdule.objects.filter(username=request.user.username)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(data, 2)
    page = paginator.page(page_num)

    context = {
        'data': page,
        'page_range': paginator.page_range
    }
    
    return render(request, 'schedule/index.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('schedule.add_schdule', raise_exception=True)
def scheduleAdd(request):
    if request.method == 'GET':
        return render(request, 'schedule/add.html')
    elif request.method == 'POST':
        data = Schdule.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            username=request.user.username,
            flag=request.POST.get('flag'),
            st_date=request.POST.get('st_date'),
            ed_date=request.POST.get('ed_date'),
            st_time=request.POST.get('st_time'),
            ed_time=request.POST.get('ed_time'),
        )
        return redirect(f'{reverse("schedule:view")}?id={data.id}')


@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('schedule.change_schdule', raise_exception=True)
def scheduleMod(request):
    if request.method == 'GET':
        data = Schdule.objects.get(
            id=request.GET.get('id'),
            username=request.user.username
        )
        context = {
            'data': data
        }        
        return render(request, 'schedule/mod.html', context)
    elif request.method == 'POST':
        data = Schdule.objects.get(
            id=request.POST.get('id'),
            username=request.user.username
        )
        data.title = request.POST.get('title')
        data.content = request.POST.get('content')
        data.flag = request.POST.get('flag')
        data.st_date = request.POST.get('st_date')
        data.ed_date = request.POST.get('ed_date')
        data.st_time = request.POST.get('st_time')
        data.ed_time = request.POST.get('ed_time')
        data.save()

        return redirect(f'{reverse("schedule:view")}?id={data.id}')

@require_http_methods(['GET', 'POST'])
@login_required
@permission_required('schedule.delete_schdule', raise_exception=True)
def scheduleDel(request):
    if request.method == 'GET':
        data = Schdule.objects.get(
            id=request.GET.get('id'),
            username=request.user.username
        )
        context = {
            'data': data
        }
        return render(request, 'schedule/del.html', context)
    elif request.method == 'POST':
        Schdule.objects.get(
            id=request.POST.get('id'),
            username=request.user.username
        ).delete()
        return redirect('schedule:index')


@require_GET
@login_required
@permission_required('schedule.view_schdule', raise_exception=True)
def scheduleView(request):
    data = Schdule.objects.get(
        id=request.GET.get('id'),
        username=request.user.username
    )
    context = {
        'data': data
    }
    return render(request, 'schedule/view.html', context)
    