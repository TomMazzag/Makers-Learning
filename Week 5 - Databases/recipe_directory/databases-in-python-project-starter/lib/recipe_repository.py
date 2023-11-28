from lib.recipe import Recipe

class RecipeRepository():

    def __init__(self, connection): 
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM recipies')
        recipies = []
        for row in rows:
            recipe = Recipe(row['id'], row['name'], row['average_cooking_time'], row['rating'])
            recipies.append(recipe)
        return recipies
    
    def find(self, recipe_id):
        rows = self.connection.execute(
            'SELECT * from recipies WHERE id = %s', [recipe_id])
        row = rows[0]
        return Recipe(row['id'], row['name'], row['average_cooking_time'], row['rating'])