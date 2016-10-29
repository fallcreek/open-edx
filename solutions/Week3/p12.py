import random
def answer(seed):
  random.seed(seed)
  ns = random.randrange(4,6,1);
  nr = random.randrange(10,16,1);
  n = ns*nr;
  
  solution1 = "C({0},5)".format(n) 
  solution2 = "{0}-3".format(nr)
  solution3 = "{0}^5 - {0}".format(ns)
  solution4 = "({1}-3)*({0}^5-{0})".format(ns,nr)
  solution5 = "({1}-3)*({0}^5-{0})/C({2},5)".format(ns,nr,n)
  
  solutions = [solution1,solution2,solution3,solution4,solution5]
  return solutions
