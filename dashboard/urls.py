from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('settings/', views.settings, name='settings'),
    path('notes/', views.note_list, name='notes'),
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_update, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_create, name='grade_add'),
    path('pomodoros/', views.pomodoro_list, name='pomodoro_list'),
    path('pomodoros/new/', views.pomodoro_create, name='pomodoro_create'),
]