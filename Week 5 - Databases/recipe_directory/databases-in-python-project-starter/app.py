from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipies.sql")

recipe_repo = RecipeRepository(connection)
recipies = recipe_repo.all()

# List them out
for recipe in recipies:
    print(recipe)


