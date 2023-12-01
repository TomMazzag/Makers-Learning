from lib.cohort import Cohort
from lib.student import Student

class CohortRepository():

    def __init__(self, connection):
        self.connection = connection

    def find_with_students(self, cohort_id):
        rows = self.connection.execute(
            "SELECT cohorts.id, cohorts.name, cohorts.start_date, students.id AS student_id, students.name AS student_name, students.cohort_id AS student_cohort_id FROM cohorts \
            JOIN students ON cohorts.id = students.cohort_id \
            WHERE cohorts.id = %s", [cohort_id]
        )
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['student_cohort_id'],)
            students.append(student)

        
        return Cohort(rows[0]['id'], rows[0]['name'], rows[0]['start_date'], students)