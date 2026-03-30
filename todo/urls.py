from django.urls import path
from todo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_task, name='add'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('toggle/<int:id>/', toggle_complete, name='toggle'),
    path('edit/<int:id>/', edit_task, name='edit'),
    path('api/tasks/', api_tasks),
]