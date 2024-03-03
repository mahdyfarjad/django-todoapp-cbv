from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User

class TestTaskView(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            email='test@test.com', password='a/123456'
        )

    def test_task_list_url_response_without_login(self):
        url = reverse('todo:task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_task_list_url_response_with_lggin(self):
        url = reverse('todo:task-list')
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)