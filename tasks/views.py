from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django import forms
from django.views.decorators.http import require_POST

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'New task...', 'class': 'input-title'}),
            'description': forms.Textarea(attrs={'rows': 2, 'class': 'input-desc', 'placeholder': 'Description (optional)'}),
        }

def task_list(request):
    # mostramos la lista y el formulario
    tasks = Task.objects.order_by('-created_at')
    form = TaskForm()
    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form})

@require_POST
def task_create(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    # Redirigimos a la lista siempre (Post/Redirect/Get)
    return redirect('tasks:list')

def task_toggle(request, pk):
    # Toggle no necesita method restriction (puede ser POST), mejor usar POST en template
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:list')

@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:list')
