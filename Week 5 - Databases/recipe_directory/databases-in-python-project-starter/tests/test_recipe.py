from lib.recipe import *

def test_recipe_class():

    recipe = Recipe(1, "Pizza", 10, 5)
    assert recipe.id == 1
    assert recipe.name == "Pizza"
    assert recipe.average_cooking_time == 10
    assert recipe.rating == 5

def test_output():

    recipe = Recipe(1, "Pizza", 10, 5)
    assert str(recipe) == "Recipe - Pizza - 10 minutes, rated 5 stars"
