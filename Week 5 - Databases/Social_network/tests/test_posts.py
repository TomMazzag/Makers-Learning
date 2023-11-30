from lib.posts import * 

def test_user():

    post = Post(1, 'Post 1', 'This is some content', 100, 1)
    assert post.account_id == 1
    assert post.title == 'Post 1'
    assert post.content == 'This is some content'
    assert post.views == 100
    
def test_format(db_connection):
    post = Post(1, 'Post 1', 'This is some content', 100, 2, db_connection)
    assert str(post) == "Post 1 - This is some content - by Person2. Views: 100"