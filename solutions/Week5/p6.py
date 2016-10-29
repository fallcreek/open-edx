import random
def answer(seed):
  random.seed(seed)
  # variable names and values
  # if multiple variables, the number of values to test should be the same
  variable_values = {'p':[0.1, 0.2, 0.3]}
  
  # value index used to extract hint
  index_of_test_value = 2
  
  solution1 = "0.3*(1-0.3)"
  solution2 = "(1 + 2 + 3 + 4)/4"
  solution3 = "(1+4+9+16)/4"
  solution4 = "1.25"
  solution5 = "(2.25 + 0.25 + 0.25 + 2.25)/4"
  
  solutions = [solution1, solution2, solution3, solution4, solution5]  
  return solutions
