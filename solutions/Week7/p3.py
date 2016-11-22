import random
def answer(seed):
  random.seed(seed)
  # variable names and values
  # if multiple variables, the number of values to test should be the same
  variable_values = {'p':[0.1,0.2,0.3]}
  
  F1 = "1/36"
  F2 = "2/36"
  F3 = "3/36"
  F4 = "4/36"
  F5 = "5/36"
  F6 = "6/36"
  
  # random variables
  r = random.randrange(3,6,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "p"
  solution2 = "p(1-p)"
  solution3 = "(1+2+3+4+5+6)/6"
  solution4 = "((1-3.5)^2 + (2-3.5)^2 + (3-3.5)^2 + (4-3.5)^2 + (5-3.5)^2 + (6-3.5)^2)/6"
  solution5 = "2*({0})".format(solution3)
  solution6 = "2*({0})".format(solution4)
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4, solution5, solution6]
  return solutions
