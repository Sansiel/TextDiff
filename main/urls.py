from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('texts/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('texts/<str:slug>/', views.text_detail, name='text_detail_url'),

]
