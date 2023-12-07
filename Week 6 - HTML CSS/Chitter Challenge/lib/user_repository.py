from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        users = []
        rows = self._connection.execute("SELECT * FROM users")
        for row in rows:
            user = User(row['id'], row["name"], row["username"], row["email"], str(row["password"]))
            users.append(user)
        return users
    
    def create(self, user):
        rows = self._connection.execute("INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s) RETURNING id",
                                        [user.name, user.username, user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return None
    
    def delete(self, album_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [album_id])
        return None
        