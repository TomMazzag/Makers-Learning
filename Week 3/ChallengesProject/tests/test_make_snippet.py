from lib.diary import make_snippet

def test_red():

    test_string = make_snippet("red")
    assert test_string == "red"

def test_long_string():

    test_string = make_snippet("This is a longer string")
    assert test_string == 'This '