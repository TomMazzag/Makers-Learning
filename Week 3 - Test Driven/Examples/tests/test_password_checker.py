from lib.password_checker import *
import pytest

def test_working_password():

    password = PasswordChecker()
    toCheck = password.check('Str0ngPassw0rd')
    assert toCheck == True

def test_not_working_password():

    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('Short')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'