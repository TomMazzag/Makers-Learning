from lib.cohort import Cohort

def test_created():

    cohort = Cohort(1, 'October', '01/10/23')
    assert cohort.id == 1
    assert cohort.name == 'October'
    assert cohort.start_date == '01/10/23'