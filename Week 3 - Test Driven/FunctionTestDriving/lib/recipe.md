# Excersise 1 - Reading Time

## 1. Describe the Problem

Assuming the user can write 200 words per minute, return the time taken to read
the string inputted

## 2. Design the Function Signature

```python
def estimated_reading_time(text):
    # words_per_minute = 200
    # reading_time = length of words in text / words per minute
    # Return:
    #   reading_time
    #   f string of minutes and seconds
    #   E.g. 5 minutes and 10 seconds
    pass
```

## 3. Create Examples as Tests

```python
'''
If text has 450 words
It will return 2 minutes and 15 seconds
'''
result = estimated_reading_time('450 word string')
'Estimated time: 2 minutes and 15 seconds'
'''
If text has no words
Return no words
'''
result = estimated_reading_time('')
'No words inputted'
```

# Excersise 2 - Correct Grammar

## 1. Describe the Problem

Verify text starts with a capital letter and ends with a suitable sentance ending punctuation mark

## 2. Design the Function Signature

```python
def grammar(text):
    #is first character upper
    #is last character suitable
    #return a string saying if valid or not
    pass
```

## 3. Create Examples as Tests

```python
'''
If text is valid
return valid string
'''
result = estimated_reading_time('This is a test!')
'The text enteres starts with a capital letter and ends with correct punctuation'

'''
If text has no words
Return invalid
'''
result = estimated_reading_time('')
'Invalid, add some text'

'''
If text is invalid
Return invalid and where invalid
'''
result = estimated_reading_time('Incorrect string')
'Invalid, missing correct '
```

# Challenge - Track todo

## 1. Describe the Problem

Working if a task needs doing using #Todo in string

## 2. Design the Function Signature

```python
def todo(text):
    # if #todo in text
    # return 'Still needs doing'
    pass
```

## 3. Create Examples as Tests

```python
'''
If #todo
# return Task still needs doing
'''
result = todo('Walk the dog #TODO')
'Task needs completing'

'''
If text is empty
return is empty
'''
result = todo('')
'Invalid, add some text'

'''
If text doesnt contain todo
Return task complete
'''
result = todo('Complete coding challenge')
'Task complete'
```