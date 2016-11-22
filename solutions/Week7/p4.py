import random
def answer(seed):
  random.seed(seed)
  # variable names and values
  # if multiple variables, the number of values to test should be the same
  variable_values = {'p':[0.1,0.2,0.3]}
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "2"
  solution2 = "1/p"
  
  # Group all solutions into a list
  solutions = [solution1, solution2]
  return solutions
