from lib.users import User

class UserRepository():

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(row["id"], row["email_address"], row["username"])
            users.append(user)
        print(users)
        return users