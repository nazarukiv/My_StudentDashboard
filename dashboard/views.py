from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import TaskForm, NoteForm, GradeForm, PomodoroForm
from .models import Task, Note, Grade, Pomodoro
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

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'dashboard/notes_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'dashboard/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'dashboard/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'dashboard/note_confirm_delete.html', {'note': note})


@login_required
def grade_list(request):
    grades = Grade.objects.filter(user=request.user).order_by('subject')
    return render(request, 'dashboard/grades_list.html', {'grades': grades})

@login_required
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = request.user
            grade.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'dashboard/grade_form.html', {'form': form})

@login_required
def pomodoro_list(request):
    pomodoros = Pomodoro.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'dashboard/pomodoro_list.html', {'pomodoros': pomodoros})

@login_required
def pomodoro_create(request):
    if request.method == 'POST':
        form = PomodoroForm(request.POST)
        if form.is_valid():
            pomodoro = form.save(commit=False)
            pomodoro.user = request.user
            pomodoro.save()
            return redirect('pomodoro_list')
    else:
        form = PomodoroForm()
    return render(request, 'dashboard/pomodoro_form.html', {'form': form})