from django.shortcuts import render,redirect
from todo.models import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title and title.strip():
            Task.objects.create(title=title)
    return redirect('/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')