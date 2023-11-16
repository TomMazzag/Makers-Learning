from unittest.mock import Mock
from lib.secret_diary import *
import pytest

def test_an_entry_integration():
    fake_diary = Mock()
    fake_diary.contents = "This is a string"
    result = SecretDiary(fake_diary.contents)
    assert result.read() == "This is a string"

def test_locked_integration():
    fake_diary = Mock()
    fake_diary.contents = "This is a string"
    secret_diary = SecretDiary(fake_diary.contents)
    secret_diary.lock()
    
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == 'Go Away!'

def test_lock():

    fake_secret_diary = Mock()
    fake_secret_diary.locked = True

    if fake_secret_diary.locked:
        result = 'Diary is locked'
    
    assert result == 'Diary is locked'

def test_diary():

    fake_diary = Mock()
    fake_diary.contents = "This is a string"
    fake_diary.read.return_value = fake_diary.contents

    assert fake_diary.read() == "This is a string"