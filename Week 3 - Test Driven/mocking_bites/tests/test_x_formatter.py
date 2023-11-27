from lib.task import Task
from unittest.mock import Mock

def test_initialised_correctly():
    task = Task('This is a task title')
    formatter = Mock()
    formatter.task = task.title
    assert formatter.task == 'This is a task title'

def test_formatter_completed():

    task = Task('This is a task title')
    task.mark_complete()

    formatter = Mock()
    formatter.task = task

    if formatter.task.complete == True:
        formatter.format.return_value = f'[x] {formatter.task.title}'
    else:
        formatter.format.return_value = f'[ ] {formatter.task.title}'

    assert formatter.format() == '[x] This is a task title'

def test_formatter_not_completed():

    task = Task('This is a task title')

    formatter = Mock()
    formatter.task = task

    if formatter.task.complete == True:
        formatter.format.return_value = f'[x] {formatter.task.title}'
    else:
        formatter.format.return_value = f'[ ] {formatter.task.title}'

    assert formatter.format() == '[ ] This is a task title'