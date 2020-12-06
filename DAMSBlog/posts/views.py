from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully Created")
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


def posts_update(request, id=None):
    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated", extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())

    context_data = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'post_form.html', context_data)


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts_list")


