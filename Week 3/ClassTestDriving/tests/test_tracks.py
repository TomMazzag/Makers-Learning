from lib.tracks import *

def test_track():
    test = music('Tom')
    test.add("Eventaully")
    result = test.show() #returns the track given by the user 
    assert result == ['Eventaully']

def test_multiple_tracks():
    test = music('Tom')
    test.add("I wanna be yours")
    test.add("Eventually")
    test.add("Example")
    result = test.show() #returns the tracks given by the user 
    assert result == ["I wanna be yours", "Eventually", "Example"]

def test_no_tracks():
    test = music('Tom')
    result = test.show() #returns 
    assert result == "No tracks have been added"

def test_empty_track():
    test = music('Tom')
    test.add("")
    result = test.show() #returns 
    assert result == "No tracks have been added"

