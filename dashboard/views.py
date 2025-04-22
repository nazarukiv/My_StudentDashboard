from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TaskForm
from .models import Task


def home(request):
    college_tasks = Task.objects.filter(category='college').order_by('due_date')
    study_tasks = Task.objects.filter(category='study').order_by('due_date')
    fitness_tasks = Task.objects.filter(category='fitness').order_by('due_date')

    return render(request, 'dashboard/home.html', {
        'college_tasks': college_tasks,
        'study_tasks': study_tasks,
        'fitness_tasks': fitness_tasks,
    })

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'dashboard/add_task.html', {'form': form})

from django.shortcuts import render

def about(request):
    return render(request, 'dashboard/about.html')

def projects(request):
    return render(request, 'dashboard/projects.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def settings(request):
    return render(request, 'dashboard/settings.html')