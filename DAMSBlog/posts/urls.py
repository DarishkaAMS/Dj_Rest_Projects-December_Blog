from django.urls import path, include
from .views import posts_create, posts_update, posts_delete, posts_detail, posts_list


urlpatterns = [
    path('create/', posts_create, name='posts_create'),
    path('detail/', posts_detail, name='posts_detail'),
    path('list/', posts_list, name='posts_list'),
    path('update/', posts_update, name='posts_update'),
    path('delete/', posts_delete, name='posts_delete'),
]