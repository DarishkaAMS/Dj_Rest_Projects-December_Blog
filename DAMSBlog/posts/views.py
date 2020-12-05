from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()

    context = {
        'form': form,
    }
    return render(request, "post_form.html", context)


def posts_detail(request, id=None):
    instance = Post.objects.get(id=id)
    # instance = get_object_or_404(Post, title='Saturday Morning')
    context_data = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', context_data)


def posts_list(request):
    queryset = Post.objects.all()
    context_data = {
        'obj_list': queryset,
        'title': 'List'
    }
    return render(request, 'index.html', context_data)


def posts_update(request):
    return HttpResponse("<h1>Update</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")
