#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  maximum_number_of_whole_batches = 0
  for (key, value) in ingredients.items():
    ingredients[key] -= recipe[key]
    print(f"{key} - {value}\n{recipe[key]}")


  for (key, value) in ingredients.items():
      if value < 0:
        print(f"{ingredients}")
        return maximum_number_of_whole_batches
      else:
          print(f"{key} - {value}\n{recipe[key]}")
          return recipe_batches(recipe, ingredients)
  
  
  print(f"{ingredients}")
  return 0
  # while 1:





# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))





recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, 
                { 'milk': 138, 'butter': 48, 'flour': 51 })