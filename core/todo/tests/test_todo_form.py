from django.test import SimpleTestCase, TestCase
from datetime import datetime

from ..forms import TaskForm
from accounts.models import User

class TestTaskForm(TestCase):
    
    def test_task_form_with_valid_data(self):
        user_obj = User.objects.create_user(email='testadmin@test.com', password='a/123456')
        form = TaskForm(data={
            'user': user_obj,
            'title':'test',
            'complete':True,
        })
        self.assertTrue(form.is_valid())
        
    def test_task_form_with_no_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())