from lib.todo import *

def test_needs_doing():
    result = todo("Walk the dog #TODO")
    assert result == 'Task needs completing'

def test_empty_string():
    result = todo("")
    assert result == 'No task given'

def test_completed_task():
    result = todo("Finish coding challenge")
    assert result == 'Task has been completed'

