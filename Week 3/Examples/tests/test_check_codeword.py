from lib.check_codeword import *

def test_codeword():
    correct_word = check_codeword("horse")
    spelt_wrong_word = check_codeword("house")
    incorrect_word = check_codeword("notTheWord")

    assert correct_word == "Correct! Come in."
    assert spelt_wrong_word == "Close, but nope."
    assert incorrect_word == "WRONG!"