from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student

def test_find_with(db_connection):
    #db_connection.seed('seeds/music_library.sql')
    repository = CohortRepository(db_connection)
    result = repository.find_with_students(1)

    assert result == Cohort(1, 'October', 'October 23', [
        Student(1, 'Tom', 1),
        Student(2, 'Mark', 1)
    ])