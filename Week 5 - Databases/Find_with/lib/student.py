class Student():

    def __init__(self, id, name, cohort_id):
        self.id= id
        self.name = name
        self.cohort_id = cohort_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Student - {self.name}, id - {self.id}, cohort - {self.cohort_id}"