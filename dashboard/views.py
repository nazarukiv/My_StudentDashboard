from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = request.user
    college_tasks = Task.objects.filter(user=user, category='college')
    study_tasks = Task.objects.filter(user=user, category='study')
    fitness_tasks = Task.objects.filter(user=user, category='fitness')

    today = timezone.now().date()
    return render(request, 'home.html', {
        'college_tasks': college_tasks,
        'study_tasks': study_tasks,
        'fitness_tasks': fitness_tasks,
        'today': today,
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # assign to current user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

from django.shortcuts import render

def about(request):
    return render(request, 'dashboard/about.html')

def projects(request):
    return render(request, 'dashboard/projects.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def settings(request):
    return render(request, 'dashboard/settings.html')