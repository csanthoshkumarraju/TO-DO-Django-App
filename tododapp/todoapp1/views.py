from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list_view(request):
    todos = Todo.objects.filter(completed=False)
    completed_todos = Todo.objects.filter(completed=True)
    return render(request, 'todo_list.html', {'todos': todos, 'completed_todos': completed_todos})

def add_todo_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
            return redirect('todo_list')
    return render(request, 'todo_list.html')

def edit_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
            return redirect('todo_list')
    return render(request, 'edit_todo.html', {'todo': todo})

def complete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todo_list')
