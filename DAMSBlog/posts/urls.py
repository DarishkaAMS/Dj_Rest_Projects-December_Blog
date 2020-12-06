from django.urls import path, include
from .views import posts_create, posts_update, posts_delete, posts_detail, posts_list


urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('create/', posts_create, name='posts_create'),
    path('<int:id>', posts_detail, name='posts_detail'),
    path('<int:id>/edit/', posts_update, name='posts_update'),
    path('<int:id>/delete/', posts_delete, name='posts_delete'),
]
