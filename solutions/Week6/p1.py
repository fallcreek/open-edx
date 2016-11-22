import random
def answer(seed):
  random.seed(seed)
  a = random.randint(1,5);
  b = random.randint(6,10);
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "{0}*(1+1/2+1/3+1/4+1/5)".format(a)
  solution2 = "{0}*(1+1/4+1/9+1/16+1/25)".format(b)
  solution3 = "{0}*(1-1/2+1/3-1/4+1/5)".format(a)
  solution4 = "{0}*(1+1/4+1/9+1/16+1/25)".format(b)
  solution5 = "{0}*(1-2/2+1/3-2/4+1/5)".format(a)
  solution6 = "{0}*(1+1/9+1/25) +{0}*4*(1/4+1/16)".format(b)
  
  
  # Group all solutions into a list
  solutions = [solution1,solution2,solution3,solution4,solution5,solution6]  
  return solutions
