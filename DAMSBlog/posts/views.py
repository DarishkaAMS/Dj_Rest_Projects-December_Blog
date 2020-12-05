from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def posts_create(request):
    return HttpResponse("<h1>Create</h1>")


def posts_detail(request):
    return HttpResponse("<h1>Detail</h1>")


def posts_list(request):
    return render(request, 'index.html', {})
    # return HttpResponse("<h1>List</h1>")


def posts_update(request):
    return HttpResponse("<h1>Update</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")
