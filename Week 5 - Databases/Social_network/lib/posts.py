class Post():

    def __init__(self, id, title, content, views, account_id, connect=False):
        self.id = id
        self.account_id = account_id
        self.title = title
        self.content = content
        self.views = views
        self.connect = connect

    def __repr__(self):
        name = self.account_id
        if self.connect != False:
            usernames = self.connect.execute("SELECT username FROM users")
            name = (usernames[self.account_id - 1]['username'])
        return f"{self.title} - {self.content} - by {name}. Views: {self.views}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__



