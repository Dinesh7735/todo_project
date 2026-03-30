from django.shortcuts import render,redirect
from todo.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    tasks_list = Task.objects.filter(user=request.user)
    query = request.GET.get('q')
    if query:
        tasks_list = tasks_list.filter(title__icontains = query)
    paginator = Paginator(tasks_list, 5)  # 5 tasks per page
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title and title.strip():
            Task.objects.create(title=title, user=request.user)
    return redirect('/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('/login/')
    
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login/')


def toggle_complete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def edit_task(request, id):
    task = Task.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
        return redirect('/')

    return render(request, 'edit.html', {'task': task})

@api_view(['GET'])
def api_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)