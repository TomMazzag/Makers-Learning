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
