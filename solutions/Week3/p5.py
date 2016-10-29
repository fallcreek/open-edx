import random
def answer(seed):
  random.seed(seed)
  n = random.randrange(10,20,1)
  
  solution1 = "{0}!/({0}-3)!".format(n)
  
  solutions = [solution1]
  return solutions
