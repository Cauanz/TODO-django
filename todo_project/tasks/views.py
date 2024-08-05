from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
   tasks = Task.objects.all()
   return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_task(request):
   if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('tasks:list')
   else:
      form = TaskForm()
   return render(request, 'tasks/task_form.html', {'form': form})