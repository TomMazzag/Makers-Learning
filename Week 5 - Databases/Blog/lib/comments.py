class Comment():

    def __init__(self, id, name, content, post_id):
        self.id= id
        self.name = name
        self.content = content
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{self.name} - {self.content}"