from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

from urllib.parse import quote_plus

from .models import Post
from .forms import PostForm


# Create your views here.


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        # if not request.user.is_authenticated:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get('title'))
        instance.user = request.user
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
    share_str = quote_plus(instance.content)
    context_data = {
        'title': instance.title,
        'instance': instance,
        'share_str': share_str,
    }
    return render(request, 'post_detail.html', context_data)


def posts_list(request):
    queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()) # all()  # .order_by('-timestamp')
    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page.
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context_data = {
        'obj_list': queryset,
        'title': 'List'
    }
    # return render(request, 'post_list.html', {'page_obj': page_obj})
    return render(request, 'post_list.html', context_data)


def posts_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts_list")
