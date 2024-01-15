from django.shortcuts import render, redirect
from .models import todo
from datetime import date

# Create your views here.

def home(request):
    if request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == "add":
            task = request.POST.get('task')
            new_task = todo(name=task, date_added=date.today())
            new_task.save()
            return redirect('home')
        elif action_type == "edit":
            id = request.POST.get('id')
            get_task = todo.objects.get(id=id)
            all_task = todo.objects.filter()
            context = {
                'todos': all_task,
                'task': get_task
            }
            return render(request, 'todoapp/home.html', context)
        elif action_type == 'save':
            task = request.POST.get('task')
            id = request.POST.get('id')
            save_task = todo(name=task, id=id, date_added=date.today())
            save_task.save()
            return redirect('home')
        elif action_type == 'delete':
            id = request.POST.get('id')
            get_task = todo.objects.get(id=id)  # delete todo by id
            get_task.delete()
            return redirect('home')

    all_task = todo.objects.filter()
    context = {
        'todos': all_task
    }
    return render(request, 'todoapp/home.html', context)


