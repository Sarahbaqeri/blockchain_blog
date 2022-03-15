from django.urls import path
from . import views


urlpatterns =[
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostIdDetail.as_view(), name='post_id'),
    path('add/', views.AddPost.as_view(), name='post_creat'),
    path('<int:pk>/edit', views.EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
]