import random
def answer(seed):
  random.seed(seed)
  R1=random.randrange(7,15,1)    # number of cards
  R2=random.randrange(2,R1-1,1)    # number of envelopes
  
  solution1 = "{1}^{{{0}}}".format(R1,R2)
  solution2 = "C({0}+{1}-1,{0})".format(R1,R2)
  solution3 = "C({0}-1,{0}-{1})".format(R1,R2)
  
  solutions = [solution1, solution2, solution3]
  return solutions
