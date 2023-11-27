from lib.todo import *

def test_name_and_task():

    todo = ToDo_list("Tom")
    todo.add("Walk the dog")
    result = todo.show() 
    assert result == 'Toms ToDo list: Walk the dog'

def test_nothing_to_do():
    todo = ToDo_list("Tom")
    result = todo.show() 
    assert result == "You have nothing left todo Tom!"

def test_empty_task():
    todo = ToDo_list("Tom")
    todo.add("")
    result = todo.show() 
    assert result == "You have nothing left todo Tom!"

def test_multiple_tasks():

    todo = ToDo_list("Tom")
    todo.add("Walk the dog")
    todo.add("Finish coding challenge")
    result = todo.show() 
    assert result == 'Toms ToDo list: Walk the dog, Finish coding challenge'

def test_multiple_tasks():

    todo = ToDo_list("Tom")
    todo.add("Walk the dog")
    todo.add("Finish coding challenge")
    todo.complete('Walk the dog')
    result = todo.show() 
    assert result == 'Toms ToDo list: Finish coding challenge'
