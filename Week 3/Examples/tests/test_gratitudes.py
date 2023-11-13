from lib.gratitudes import *

def test():

    message = Gratitudes()
    message.add('family')
    message.add('friends')

    assert message.format() == 'Be grateful for: family, friends'