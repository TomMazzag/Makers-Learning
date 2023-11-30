from lib.user_repo import *
from lib.users import User

def test_all(db_connection):
    all_users = UserRepository(db_connection)
    assert all_users.all() == [
        User(1, 'example@test.com', 'Person1'),
        User(2, 'example@makers.com', 'Person2'),
        User(3, 'example@databases.com', 'Person3')
    ]