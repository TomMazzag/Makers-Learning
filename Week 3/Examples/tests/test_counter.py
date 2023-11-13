from lib.counter import *

def test_coutner():

    test = Counter()
    test.add(8)
    answer = test.report()
    assert answer == "Counted to 8 so far."

def test_coutner2():

    test = Counter()
    test.add(4)
    test.add(7)
    answer = test.report()
    assert answer == "Counted to 11 so far."