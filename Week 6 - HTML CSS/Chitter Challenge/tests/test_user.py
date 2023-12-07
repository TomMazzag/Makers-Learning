from lib.user import User
from lib.user_repository import UserRepository

def test_user_class():

    tom = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    assert tom.name == "Tom"
    assert tom.username == "TomMazzag"
    assert tom.email == "tom@mazzag.com"
    assert tom.password == "testPassw0rd"
    assert str(tom) == "User(Tom, TomMazzag, tom@mazzag.com, testPassw0rd)"

def test_eqaul():
    tom = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    tom1 = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    assert tom == tom1

def test_add_to_db(db_connection):
    db_connection.seed('seeds/users_table.sql')
    repository = UserRepository(db_connection)

    tom = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    repository.create(tom)
    
    assert repository.all() == [
        User(1, "Anonymous", "AnonymousUser", "anon@user.com", "None"),
        User(2, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    ]
