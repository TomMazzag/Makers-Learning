from lib.post_repository import PostRepository
from lib.posts import Post
from lib.comments import Comment
def test_find_with(db_connection):
    #db_connection.seed('seeds/music_library.sql')
    repository = PostRepository(db_connection)
    result = repository.find_with_comments(1)

    assert result == Post(1, 'First Post', 'This is a first post', [
        Comment(1, 'Tom', 'This is a great post!', 1),
        Comment(2, 'User2', 'This is a good first post', 1),
        Comment(3, 'User3', 'This is a good first post', 1)
    ])