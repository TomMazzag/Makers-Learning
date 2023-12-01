from lib.posts import Post

def test_created():

    post = Post(1, 'Title', 'Content')
    assert post.id == 1
    assert post.title == 'Title'
    assert post.content == 'Content'

def test_format():

    post = Post(1, 'Title', 'Content')
    assert str(post) == 'Title - Content'

def test_eqaul():

    post = Post(1, 'Title', 'Content')
    post1 = Post(1, 'Title', 'Content')
    assert post == post1
