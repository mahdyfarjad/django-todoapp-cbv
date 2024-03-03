from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from todo.models import Task
from .serializer import TaskSerializer
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# from .paginations import MyPagination

class TaskModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().filter(user=self.request.user)
        return queryset