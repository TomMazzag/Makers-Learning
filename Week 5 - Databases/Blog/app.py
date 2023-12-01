from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository
import time

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()

  def run(self):
    print("Welcome to this social media playform, what would you like to do?")
    print("1 - Get comments for a post")
    print("2 - Add comments to a post")
    option = int(input('1 or 2? '))
    time.sleep(1)
    post_repository = PostRepository(self._connection)

    if option == 1:
      find_comments_on_post(post_repository)
    else:
      post_number = post_repository.posts_to_comment_on()
      name = input('What username? ')
      comment = input('Comment: ')
      post_repository.add_to_post(post_number, name, comment)


def find_comments_on_post(post_repository):
  choice = int(input("Enter your choice of post: "))
  result = post_repository.find_with_comments(choice)
  print(f'\n\n{result}')
  print('Comments:')
  time.sleep(1)
  for comment in result.comments:
    print(f'{comment.name} - {comment.content}')


if __name__ == '__main__':
    app = Application()
    app.run()
