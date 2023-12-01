from lib.comments import Comment

def test_created():

    comment = Comment(1, 'Tom', 'This is a great post', 1)
    assert comment.id == 1
    assert comment.name == 'Tom'
    assert comment.content == 'This is a great post'
    assert comment.post_id == 1

def test_format():
    
    comment = Comment(1, 'Tom', 'This is a great post', 1)
    assert str(comment) == 'Tom - This is a great post'

def test_equal():

    comment = Comment(1, 'Tom', 'This is a great post', 1)
    comment1 = Comment(1, 'Tom', 'This is a great post', 1)
    assert comment == comment1