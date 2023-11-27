from lib.track import Track

def test_match_track():
    track1 = Track("Title", "Artist")
    assert track1.matches('Title') == True

def test_match_artist():
    track1 = Track("Title", "Artist")
    assert track1.matches('Artist') == True

def test_false():
    track1 = Track("Title", "Artist")
    assert track1.matches('blank') == False

def test_match_track_partial():
    track1 = Track("Mock title", "Artist")
    assert track1.matches('Moc') == True

def test_match_artist_partial():
    track1 = Track("Title", "Artist")
    assert track1.matches('Art') == True