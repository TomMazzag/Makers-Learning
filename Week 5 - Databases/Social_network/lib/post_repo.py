from lib.posts import Post

class PostRepository():

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            posts.append(post)
        return posts
    
    def views(self, post):
        rows = self.connection.execute("SELECT id, views FROM posts")
        for row in rows:
            if row['id'] == post:
                return row['views']
        return 'Post not found'