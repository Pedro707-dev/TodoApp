import pytest
from tasks.models import Task

@pytest.mark.django_db
def test_task_creation():
    t = Task.objects.create(title='Test', description='Desc')
    assert t.pk is not None
    assert t.title == 'Test'
    assert t.completed is False
