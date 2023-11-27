from lib.music_library import *
from lib.track import *

def test():
    library = MusicLibrary()
    track_1 = Track('Title 1', 'Artist 1')
    track_2 = Track('Title 2', 'Artist 2')
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

def test_for_search():
    library = MusicLibrary()
    track_1 = Track('Title 1', 'Artist 1')
    track_2 = Track('Title 2', 'Artist 2')
    library.add(track_1)
    library.add(track_2)
    assert library.search('Title 1') == [track_1]