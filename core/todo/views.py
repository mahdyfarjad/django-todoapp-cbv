from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    # model = Task
    login_url = reverse_lazy('accounts:login-user')
    template_name = 'todo/main.html'
    context_object_name = 'tasks'
    

    def get_queryset(self):
        # return the latest tasks
        queryset = Task.objects.all().filter(user=self.request.user).order_by('-created_date')
        return queryset

def CreateTask(request):
    title = request.POST['title']
    Task.objects.create(user=request.user, title=title)
    return redirect('todo:task-list')

def CompleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.complete:
        return redirect('todo:task-list')
    
    task.complete = True
    task.save()
    return redirect('todo:task-list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:task-list')