from lib.greet import *

def test_greet():
    greeting = greet('Tom')
    assert greeting == "Hello, Tom!"