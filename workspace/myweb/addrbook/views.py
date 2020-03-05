from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from addrbook.models import AddressBook

# Create your views here.
@require_GET
@login_required
def addrIndex(request):
    data = AddressBook.objects.all()
    context = {
        'data': data
    }
    return render(request, 'addrbook/index.html', context)


@require_GET
@login_required
def addrView(request):
    data = AddressBook.objects.get(id=request.GET.get('id'))
    context = {
        'data': data
    }
    return render(request, 'addrbook/view.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def addrAdd(request):
    if request.method == 'GET':
        return render(request, 'addrbook/add.html')
    elif request.method == 'POST':
        AddressBook.objects.create(
            name=request.POST.get('name'),
            company=request.POST.get('company'),
            age=request.POST.get('age'),
            relation=request.POST.get('relation'),
            phone_addr=request.POST.get('phone_addr'),
            email=request.POST.get('email'),
            brithday=request.POST.get('brithday')
        )
        return redirect('/addrbook/')


@require_http_methods(['GET', 'POST'])
@login_required
def addrMod(request):
    if request.method == 'GET':
        data = AddressBook.objects.get(id=request.GET.get('id'))
        context = {
            'data': data
        }
        
        return render(request, 'addrbook/mod.html', context)
    elif request.method == 'POST':
        data = AddressBook.objects.get(id=request.POST.get('id'))
        data.name = request.POST.get('name')
        data.company = request.POST.get('company')
        data.age = request.POST.get('age')
        data.relation = request.POST.get('relation')
        data.phone_addr = request.POST.get('phone_addr')
        data.email = request.POST.get('email')
        data.brithday = request.POST.get('brithday')
        data.save()

        return redirect(f'/addrbook/view/?id={data.id}')


@require_http_methods(['GET', 'POST'])
@login_required
def addrDel(request):
    if request.method == 'GET':
        data = AddressBook.objects.get(id=request.GET.get('id'))
        context = {
            'data': data
        }
        return render(request, 'addrbook/del.html', context)
    elif request.method == 'POST':
        data = AddressBook.objects.get(id=request.POST.get('id'))
        data.delete()
        return redirect('/addrbook/')

        
