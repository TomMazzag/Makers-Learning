from lib.posts import Post
from lib.comments import Comment

class PostRepository():

    def __init__(self, connection):
        self.connection = connection

    def find_with_comments(self, post_id):
        rows = self.connection.execute(
            "SELECT posts.id, posts.title, posts.content, comments.id AS comment_id, comments.name, comments.content AS comment, comments.post_id FROM posts \
            JOIN comments ON posts.id = comments.post_id \
            WHERE posts.id = %s", [post_id]
        )
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['name'], row['comment'], row['post_id'])
            comments.append(comment)


        return Post(rows[0]['id'], rows[0]['title'], rows[0]['content'], comments)
    
    def add_post(self, title, content):
        self.connection.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s)", [title, content]
        )
        return None
    
    def posts_to_comment_on(self):
        id_dict = self.connection.execute('SELECT id FROM posts')
        ids = [id['id'] for id in id_dict]
        post_id = input(f'Which post would you like to comment on? {ids}: ')
        return post_id

    def add_to_post(self, post_id, name, content):
        self.connection.execute(
            "INSERT INTO comments (name, content, post_id) VALUES (%s, %s, %s)", [name, content, post_id],
        )
        return None
