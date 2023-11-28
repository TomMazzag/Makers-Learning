class Recipe():

    def __init__(self, id, name, average_cooking_time, rating):
        self.id = id
        self.name = name
        self.average_cooking_time = average_cooking_time
        self.rating = rating
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Recipe - {self.name} - {self.average_cooking_time} minutes, rated {self.rating} stars"