## 1. Describe the Problem

Keep tracks of music listened to and ass tracks listened to

## 2. Design the Class Interface

```python

class music:

    def __init__(self, name):
        # parameters:
        #   name: users name
        # self.track_list = []
        # A list of all the tracks the user has listened to

    def add(self, track)
        # parameters:
        #   track: a string of the track that should be added
        # returns:
        #   nothing
        # side-affects:
        #   track is added to track lsit

    def show(self)
        # parameters:
        #   none
        # returns:
        #   list of the users listening history
        
```

## 3. Create Examples as Tests

``` python
# EXAMPLE

"""
If the user adds a name and a track
Track is returned
"""
test = music('Tom')
test.add("")
test.show() #returns the track given by the user 

"""
If the user adds a name and multiple tracks
Tracks are returned
"""
test = music('Tom')
test.add("")
test.add("")
test.add("")
test.show() #returns the tracks given by the user 

"""
If the user adds a name and no tracks
Returns no tracks added
"""
test = music('Tom')
test.show() #returns "No tracks have been added"

```

