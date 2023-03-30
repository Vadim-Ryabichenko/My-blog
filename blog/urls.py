from django.urls import path
from . import views



urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('about-me/', views.second_page, name='second_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]