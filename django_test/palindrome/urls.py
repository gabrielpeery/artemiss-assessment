from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('history', views.palindromeHistory, name='history'),
  path('bulk/', views.bulk, name='bulk'),
  path('<str:checkString>', views.checkString, name='checkString'),
]
