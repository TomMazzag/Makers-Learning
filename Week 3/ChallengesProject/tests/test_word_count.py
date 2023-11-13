from lib.diary import count_words

def test_words_3():

    test = count_words("3 word string")
    assert test == 3

def test_one_word():

    test = count_words("Word")
    assert test == 1

def test_no_words():

    test = count_words("")
    assert test == 0