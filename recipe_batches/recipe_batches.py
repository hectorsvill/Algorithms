#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  maximum_number_of_whole_batches = 0
  while True:
    for (key, value) in ingredients.items():
      ingredients[key] -= recipe[key]
      
      if ingredients[key] < 0:
        return maximum_number_of_whole_batches
      
      print(f"{key} - {value}\n{recipe[key]}")
     
    maximum_number_of_whole_batches += 1
      


  # for (key, value) in ingredients.items():
  #     if value < 0:
  #       print(f"{ingredients}")
  #       return maximum_number_of_whole_batches
  #     else:
  #         print(f"{key} - {value}\n{recipe[key]}")

  
  
  print(f"{ingredients}")
  return 0
  # while 1:


x2 = recipe_batches({'milk': 2}, {'milk': 100})

# x3 = recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, 
#                 { 'milk': 138, 'butter': 48, 'flour': 51 })

print(x2)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))



