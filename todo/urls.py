from django.urls import path
from todo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_task, name='add'),
    path('delete/<int:id>/', delete_task, name='delete'),
]