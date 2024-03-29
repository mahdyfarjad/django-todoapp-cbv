from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.TaskListView.as_view(), name='task-list'),
    path('create/', views.CreateTask, name='create-task'),
    path('complete/<int:pk>/', views.CompleteTask, name='complete-task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-task'),
    path('api/v1/', include('todo.api.v1.urls')),

]