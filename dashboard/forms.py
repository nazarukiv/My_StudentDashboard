from django import forms
from .models import Task, Grade, Pomodoro


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_completed', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'assignment', 'grade']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'assignment': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PomodoroForm(forms.ModelForm):
    class Meta:
        model = Pomodoro
        fields = ['task_name', 'duration_minutes']