from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
   path('', views.task_list, name='list'),
   path('create/', views.create_task, name="create_task"),
   path('tasks/<int:task_id>/complete/', views.complete_task, name="complete_task"),
   path('tasks/<int:task_id>/remove/', views.remove_task, name="remove_task")
]
