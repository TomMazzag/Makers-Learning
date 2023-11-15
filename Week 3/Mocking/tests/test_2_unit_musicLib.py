from unittest.mock import Mock
from lib.music_library import MusicLibrary


def test_search():

    library = MusicLibrary()
    test1 = mock_test_1()
    library.add(test1)
    test2 = mock_test_2()
    library.add(test2)
    assert library.search("Test") == [test2]

class mock_test_1():
    def matches(self, keyword):
        return False
    
class mock_test_2():
    def matches(self, keyword):
        return True
    
def test_search_without_classes():

    library = MusicLibrary()
    test1 = Mock()
    test1.matches.return_value = True
    library.add(test1)
    test2 = Mock()
    test2.matches.return_value = False
    library.add(test2)
    assert library.search("Test") == [test1]