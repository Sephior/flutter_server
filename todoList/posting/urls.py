from django import views
from django.urls import path

from posting import views

urlpatterns = [
    path('addTask', views.addTask, name='addTask')
]