def todo(text):

    if len(text) < 1:
        return 'No task given'
    
    if '#TODO' in text:
        return 'Task needs completing'
    
    return 'Task has been completed'