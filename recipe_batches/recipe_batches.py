#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_batches = float('Inf')
  for key in recipe:
    if ingredients.get(key):
      min_batches = min(ingredients[key] // recipe[key], min_batches)
    else: return 0
  return min_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 20, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))