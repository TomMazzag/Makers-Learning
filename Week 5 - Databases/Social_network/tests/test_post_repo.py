from lib.post_repo import PostRepository
from lib.posts import Post

def test_all_posts(db_connection):
    all_posts = PostRepository(db_connection)
    assert all_posts.all() == [
        Post(1, 'First post', 'This is a first post', 19, 1),
        Post(2, 'Second post', 'This is a second post', 9, 1),
        Post(3, 'Third post', 'This is a third post', 15, 1),
        Post(4, 'Fourth post', 'This is a fourth post', 3, 2),
    ]

def test_views(db_connection):
    posts = PostRepository(db_connection)
    assert posts.views(2) == 9

def test_wrong_post_views(db_connection):
    posts = PostRepository(db_connection)
    assert posts.views(5) == 'Post not found'