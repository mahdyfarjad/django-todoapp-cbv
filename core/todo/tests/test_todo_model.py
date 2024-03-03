from django.test import TestCase
from accounts.models import User

from ..models import Task



class TestTodoModel(TestCase):
    def setUp(self):
        self.user_obj = User.objects.create_user(email='test@test.com', password='a/123456')
        
    def tets_create_task_with_valid_data(self):

        task = Task.objects.create(    
            user= self.user_obj,
            title= 'test',
        )
        # self.assertEqual(task.title, 'test')
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
