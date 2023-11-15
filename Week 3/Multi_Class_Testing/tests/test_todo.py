from lib.todo import *
from lib.todo_list import *

def test_add_to_and_complete():

    task1 = Todo("Complete this task")
    task2 = Todo("Walk the dog")
    task3 = Todo("Make lunch")

    test = TodoList()

    test.add(task1)
    test.add(task2)
    test.add(task3)

    task2.mark_complete()

    result = test.complete()
    assert result == [task2.task]

def test_complete_all_tasks():

    task1 = Todo("Complete this task")
    task2 = Todo("Walk the dog")
    task3 = Todo("Make lunch")

    test = TodoList()

    test.add(task1)
    test.add(task2)
    test.add(task3)

    test.give_up()

    result = test.complete()
    assert result == [task1.task, task2.task, task3.task]

def test_none_complete():

    task1 = Todo("Complete this task")
    task2 = Todo("Walk the dog")
    task3 = Todo("Make lunch")

    test = TodoList()

    test.add(task1)
    test.add(task2)
    test.add(task3)


    result = test.incomplete()
    assert result == [task1.task, task2.task, task3.task]