from lib.reading_time import *

def test_200_words():
    words_x = "words " * 200
    test = estimated_reading_time(words_x)
    assert test == 'Estimated reading time: 1 minute'

def test_50_words():
    words_x = "words " * 50
    test = estimated_reading_time(words_x)
    assert test == 'Estimated reading time: 15 seconds'

def test_no_words():
    words_x = ""
    test = estimated_reading_time(words_x)
    assert test == 'No words in input'