from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
def aboutMain(request):
    context = {
        'key': '동적 데이터를 템플릿에 삽입',
        'int': 1000000,
        'list': [1, 2, 3],
        'dict': {'a': 1, 'b': 2},
        'htm_code': '<h1>HTML 코드가 있는 데이터입니다</h1>',
    }
    return render(request, 'about/index.html', context)

@require_GET
def aboutDjango(request):
    if request.method == 'GET':
        context = {
            'method': request.method,
            'get_data': request.GET,
            'version': request.GET.get('version'),
            'project': request.GET.get('project'),
        }
    elif request.method == 'POST':
        context = {
            'method': request.method,
            'get_data': request.POST,
            'version': request.POST.get('version'),
            'project': request.POST.get('project'),
        }
    return render(request, 'about/django.html', context)