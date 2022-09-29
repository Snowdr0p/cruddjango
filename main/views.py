from django.shortcuts import render
from django.http import HttpResponse
from .models import Transport


def index(request):
    return render(request, 'main/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        can_move = bool(request.POST.get('can_move'))
        transport = Transport(name=name, description=description, can_move=can_move)
        transport.save()

    return render(request, 'main/create.html')


def read(request):
    transport = Transport.objects.all()
    context = {
        'transport': transport,
    }
    return render(request, 'main/read.html', context=context)


def update(request):
    if request.method == 'POST':
        pk = int(request.POST.get('pk'))
        t = Transport.objects.get(pk=pk)
        if t:
            t.name = request.POST.get('name')
            t.description = request.POST.get('description')
            t.can_move = bool(request.POST.get('can_move'))
            t.save()

    transport = Transport.objects.all()
    context = {
        'transport': transport,
    }
    return render(request, 'main/update.html', context)


def delete(request):
    if request.method == 'POST':
        pk = int(request.POST.get('pk'))
        t = Transport.objects.get(pk=pk)
        if t:
            t.delete()

    transport = Transport.objects.all()
    context = {
        'transport': transport,
    }
    return render(request, 'main/delete.html', context=context)
