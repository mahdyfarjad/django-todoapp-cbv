import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
from todo.models import Task

@pytest.fixture
def common_user():
    user = User.objects.create_user(email="test@test.com", password="a/123456")
    return user


@pytest.mark.django_db
class TestTaskApi:
    client = APIClient()

    def test_get_task_list_response_403(self):    
        url = reverse('todo:api_v1:task-list')
        response = self.client.get(url)
        assert response.status_code == 403

    def test_get_task_list_response_200(self, common_user):
        url = reverse('todo:api_v1:task-list')
        self.client.force_login(user=common_user)
        response = self.client.get(url)
        assert response.status_code == 200

    def test_post_create_task_response_403(self, common_user):
        url = reverse('todo:api_v1:task-list')
        data = {
            'user':common_user,
            'title': 'test',
        }
        response = self.client.post(url, data)
        assert response.status_code == 403

    def test_post_create_task_response_201(self, common_user):
        url = reverse('todo:api_v1:task-list')
        self.client.force_login(user=common_user)
        data = {
            'title': 'test',
        }
        response = self.client.post(url, data)
        assert response.status_code == 201

    def test_get_task_detail_response_403(self):
        url = reverse('todo:api_v1:task-detail', kwargs={"pk":1})
        response = self.client.get(url)
        assert response.status_code == 403
    
    def test_get_task_detail_response_200(self, common_user):
        url = reverse('todo:api_v1:task-detail', kwargs={"pk":1})
        self.client.force_login(user=common_user)
        response = self.client.get(url)
        assert response.status_code == 200
        # متوجه نمیشم چرا 404 برمیگدونه!!