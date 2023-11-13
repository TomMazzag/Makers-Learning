from lib.present import *
import pytest

def test_unwrap():

    gift = Present()

    with pytest.raises(Exception) as err:
        gift.unwrap()
    error_message = str(err.value)
    assert error_message == 'No contents have been wrapped.'

def test_wrap():

    present = Present()
    present.wrap('Gift')

    assert present.unwrap() == 'Gift'

def test_wrap_error():

    present = Present()
    present.wrap('Gift')
    with pytest.raises(Exception) as e:
        present.wrap('Gift2')
    err_message = str(e.value)
    assert err_message == 'A contents has already been wrapped.'