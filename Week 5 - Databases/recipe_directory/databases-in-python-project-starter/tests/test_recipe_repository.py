from lib.recipe_repository import *
from lib.recipe import *

def test_all(db_connection):
    db_connection.seed("seeds/recipies.sql") 
    repository = RecipeRepository(db_connection)
    
    recipies = repository.all()
    assert recipies == [
        Recipe(1, 'Pizza', 10 , 5),
        Recipe(2, 'Spaghetti', 15 , 3),
        Recipe(3, 'Chilli', 20 , 4),
        Recipe(4, 'Wrap', 5 , 2),
        Recipe(5, 'Sandwich', 1 , 4)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/recipies.sql") 
    repository = RecipeRepository(db_connection)
    
    result = repository.find(1)
    assert result == Recipe(1, 'Pizza', 10 , 5)
    