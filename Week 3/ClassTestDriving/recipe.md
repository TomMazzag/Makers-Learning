## 1. Describe the Problem

Todo list

## 2. Design the Class Interface

```python

class ToDo_list:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the user name
        pass 

    def add(self, task):
        # Parameters:
        #   task: string of what to be done
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

    def list(self):
        # Returns:
        #   A list of all tasks
        # Side-effects:
        #   Tells user if their list is empty
        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
todo = ToDo_list("Tom")
todo.add("Walk the dog")
todo.list() # 'Toms list: item'

"""
Given a name and no task
Tell the user they have no more tasks
"""
todo = ToDo_list("Tom")
todo.list() # "You have nothing left todo Tom!"

"""
Given a name and an empty task
Dont add the task
Tell the user they have no more tasks
"""
todo = ToDo_list("Tom")
todo.remind_me_to("")
todo.remind() # "You have nothing left todo Tom!"
```



## 1. Describe the Problem

Todo list where tasks can be marked as done

## 2. Design the Class Interface

```python

class ToDo_list:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the user name
        pass 

    def add(self, task):
        # Parameters:
        #   task: string of what to be done
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

    def show(self):
        # Returns:
        #   A list of all tasks
        # Side-effects:
        #   Tells user if their list is empty
        pass 

    def complete(self, task):
        # Parameters:
        #   task: string
        # Side effects:
        #   Removes selected string
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

#Same as above +++

"""
Add a task
Mark it as done
"""
todo = ToDo_list("Tom")
todo.add("Walk the dog")
todo.complete("Walk the dog") 
todo.show() # returns an empty list


```





