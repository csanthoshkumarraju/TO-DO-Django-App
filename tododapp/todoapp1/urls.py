from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_list'),
    path('add/', views.add_todo_view, name='add_todo'),
    path('edit/<int:todo_id>/', views.edit_todo_view, name='edit_todo'),
    path('complete/<int:todo_id>/', views.complete_todo_view, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo_view, name='delete_todo'),
]
