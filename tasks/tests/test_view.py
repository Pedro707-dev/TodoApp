import pytest
from django.urls import reverse
from tasks.models import Task

@pytest.mark.django_db
def test_task_list_view(client):
    Task.objects.create(title='T1')
    resp = client.get(reverse('tasks:list'))
    assert resp.status_code == 200
    assert 'T1' in resp.content.decode()
