import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from task_manager.models import Task


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_list_tasks(api_client):
    url = reverse('task-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_task(api_client):
    url = reverse('task-list')
    data = {
        'title': 'Task 1',
        'description': 'Task description',
        'completed': False,
        'created_at': '2023-07-15T10:00:00Z'
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_retrieve_task(api_client):
    task = Task.objects.create(
        title='Task 1',
        description='Task description',
        completed=False,
        created_at='2023-07-15T10:00:00Z'
    )
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_update_task(api_client):
    task = Task.objects.create(
        title='Task 1',
        description='Task description',
        completed=False,
        created_at='2023-07-15T10:00:00Z'
    )
    url = reverse('task-detail', kwargs={'pk': task.pk})
    data = {
        'title': 'Updated Task',
        'description': 'Updated description',
        'completed': True,
        'created_at': '2023-07-16T10:00:00Z'
    }
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_task(api_client):
    task = Task.objects.create(
        title='Task 1',
        description='Task description',
        completed=False,
        created_at='2023-07-15T10:00:00Z'
    )
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT