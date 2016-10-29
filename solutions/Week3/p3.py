import random
def answer(seed):
  random.seed(seed)
  R = random.randrange(4,9,1)
  RL = R - 1
  
  solution1 = "{0}^4".format(R)
  solution2 = "4"
  solution3 = "({0}-1)*{0}".format(R)
  solution4 = "{0}*({0}-1)/({0}^4)".format(R)
  
  solutions = [solution1,solution2,solution3,solution4]
  return solutions
