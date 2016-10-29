import random
def answer(seed):
  random.seed(seed)
  from math import factorial as fac
  a = random.randrange(2,3,1)
  n = fac(26)/fac(26-1)
  b = random.randrange(3,6,1)
  c = b + 1
  d = int(c * fac(26)/fac(26-a) + 1)
  
  solution1 = "P(26,{0})".format(a)
  solution2 = "({1} - 1)*P(26,{0}) + 1".format(a,b)
  solution3 = "{0} + 1".format(c)
  
  solutions = [solution1, solution2, solution3]
  return solutions
