import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  import math
  
  ans1 = 0
  mu = 0 
  a = 0
  x = 0
  lambd = 0
  while (0.002 > ans1) :
      mu = random.randrange(50,70,5) / 10.
      lambd = 1. / mu
      a = random.randrange(9,12,1)
      x = lambd * a
      ans1 = math.exp(x)
      k=random.randrange(3,7,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "e^{{(-1/{0} * {1})}}".format(mu,a)
  solution2 = "e^{{(-1/{0}*10)}}*((1/{0}*10)^{{{1}}})/({1}!)".format(mu,k)
  
  # Group all solutions into a list
  solutions = [solution1,solution2]
  return solutions
