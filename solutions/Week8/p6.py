import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  a = random.randrange(10,50,1) / 10
  b = random.randrange(10,50,1) / 10
  
  while (0.5 > abs(a - b)):
      b = random.randrange(10,50,1) / 10
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "((1/2) * e^{{(-{0})}} + (1/2) * e^{{(-{1})}})".format(a,b)
  
  
  # Group all solutions into a list
  solutions = [solution1]
  return solutions
