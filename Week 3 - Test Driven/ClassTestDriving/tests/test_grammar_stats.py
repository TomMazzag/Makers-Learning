from lib.grammar_stats import *

def test_capital_and_punctuation():
    text = GrammarStats()
    result = text.check("This is a test!")
    assert result == True

def test_capital_and_no_punctuation():
    text = GrammarStats()
    result = text.check("This is a test")
    assert result == False

def test_no_capital_and_punctuation():
    text = GrammarStats()
    result = text.check("this is a test!")
    assert result == False

def test_empty_string():
    text = GrammarStats()
    result = text.check("")
    assert result == False

def test_percentage_50():
    text = GrammarStats()
    text.check("This is a test!")
    text.check("This is a test!")
    text.check("this is a test!")
    text.check("this is a test")
    result = text.percentage_good()
    assert result == '50%'

def test_percentage_100():
    text = GrammarStats()
    text.check("This is a test!")
    text.check("This is a test!")
    result = text.percentage_good()
    assert result == '100%'

def test_no_strings():
    text = GrammarStats()
    result = text.percentage_good()
    assert result == 'No strings tested'