from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository
import time

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()

  def run(self):
    print("Welcome to find students in the cohort")
    choice = int(input("Enter your choice of cohort: "))

    time.sleep(1)

    cohort_repository = CohortRepository(self._connection)
    result = cohort_repository.find_with_students(choice)
    print(f'\n\n{result}, with students:')
    time.sleep(1)
    for student in result.students:
      print(f'{student.name}, id - {student.id}')




if __name__ == '__main__':
    app = Application()
    app.run()
