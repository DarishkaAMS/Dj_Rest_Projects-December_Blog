from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def posts_create(request):
    return HttpResponse("<h1>Create</h1>")


def posts_detail(request):
    context_data = {
        'title': 'Detail'
    }
    return render(request, 'index.html', context_data)


def posts_list(request):
    context_data = {
        'title': 'List'
    }
    return render(request, 'index.html', context_data)


def posts_update(request):
    return HttpResponse("<h1>Update</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")
