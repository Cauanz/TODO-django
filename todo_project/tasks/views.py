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

def complete_task(request, task_id):
   task = get_object_or_404(Task, id=task_id) #Busca objeto (Task) cujo id seja igual o id ou retorna um 404 caso não encontre
   if request.method == 'POST':
      task.completed = not task.completed
      task.save()
      return redirect('tasks:list')
   else:
      return redirect('tasks:create_task')
   
def remove_task(request, task_id):
   task = get_object_or_404(Task, id=task_id)
   if request.method == 'POST':
      task.delete()
      return redirect('tasks:list')
   else:
      return redirect('tasks:create_task')