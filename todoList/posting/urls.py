from django.urls import path

from posting import views

urlpatterns = [
    path('', views.getTaskList, name='getTaskList'),
    path('addTask', views.addTask, name='addTask'),
    path('update/<int:pk>/<str:work>', views.updateTask, name='updateTask'),
    path('remove/<int:pk>', views.removeTask, name='removeTask'),
]