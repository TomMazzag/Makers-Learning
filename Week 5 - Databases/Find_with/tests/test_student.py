from lib.student import Student

def test_created():

    student = Student(1, 'Tom', 1)
    student2 = Student(2, 'Mark', 1)
    assert student.id == 1
    assert student.name == 'Tom'
    assert student.cohort_id == 1