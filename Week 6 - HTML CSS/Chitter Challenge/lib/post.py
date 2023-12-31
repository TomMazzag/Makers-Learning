class Post():

    def __init__(self, id, content, user_id):
        self.id = id
        self.content = content
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post{self.id} = {self.content}, USER:{self.user_id}"