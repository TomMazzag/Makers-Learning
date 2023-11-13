from lib.string_builder import *

def test_tom():

    name = StringBuilder()
    name.add("Thomas")
    assert name.output() == 'Thomas'
    assert name.size() == 6