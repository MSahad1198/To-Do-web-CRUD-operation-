from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

# Home View adn add task
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

# Mark as complete
def markComplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

# Mark as undone
def Undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

# Edit Task
def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'task': get_task,
        }
    return render(request, 'edit.html', context)

# Delete Task
def deleteTask(request, pk):
    del_task = get_object_or_404(Task, pk=pk)
    del_task.delete()
    return redirect('home')
