from lib.users import * 

def test_user():

    user = User(1, 'example@me.com', 'Tom')
    assert user.email == 'example@me.com'
    assert user.username == 'Tom'
    
def test_format():
    user = User(1, 'example@me.com', 'Tom')
    assert str(user) == "Tom, example@me.com"