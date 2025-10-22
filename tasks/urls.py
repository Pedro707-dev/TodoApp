from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('toggle/<int:pk>/', views.task_toggle, name='toggle'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]
