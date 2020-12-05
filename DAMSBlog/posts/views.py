from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def posts_create(request):
    return HttpResponse("<h1>Hello</h1>")


def posts_detail(request):
    return HttpResponse("<h1>Hello</h1>")


def posts_list(request):
    return HttpResponse("<h1>Hello</h1>")


def posts_update(request):
    return HttpResponse("<h1>Hello</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Hello</h1>")
