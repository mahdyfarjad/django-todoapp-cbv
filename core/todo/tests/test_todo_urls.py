from django.test import TestCase
from django.urls import reverse, resolve

from ..views import TaskListView, TaskDeleteView

# Create your tests here.

class TestUrl(TestCase):

    def test_todo_task_list_url_resolve(self):
        url = reverse('todo:task-list')
        self.assertEqual(resolve(url).func.view_class, TaskListView)
        
    def test_todo_task_detail_url_resolve(self):
        url = reverse('todo:delete-task', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, TaskDeleteView)