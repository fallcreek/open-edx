import random
def answer(seed):
  random.seed(seed)
  R1=random.randrange(8,15,1);
  R2=random.randrange(2,R1-2,1);
  
  solution1 = "{0} - 1".format(R1)
  solution2 = "{0}".format(R2)
  solution3 = "(({1}+{0}-1)!)/(({1})!*({0}-1)!)".format(R1,R2)
  
  solutions = [solution1, solution2, solution3]
  return solutions
