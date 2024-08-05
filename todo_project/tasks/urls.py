from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
   path('', views.task_list, name='list'),
   path('create/', views.create_task, name="create_task")
]
