from lib.correct_grammar import *

def test_empty_string():
    result = grammar('')
    assert result == 'Invalid, no text given'

def test_missing_punctuation():
    result = grammar('This is missing punctuation')
    assert result == 'Missing punctuation'

def test_missing_capital():
    result = grammar('this is missing capital letter at the start')
    assert result == 'Missing capital letter at the start'

def test_working_string():
    result = grammar('This is a working test!')
    assert result == 'Grammar is correct'