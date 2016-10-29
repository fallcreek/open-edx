import random
def answer(seed):
  random.seed(seed)
  ns = random.randrange(4,6,1)
  nr = random.randrange(10,16,1)
  n = ns*nr
  
  solution1 = "C({0},5)".format(n)
  solution2 = "{0}".format(nr)
  solution3 = "{0}-1".format(nr)
  solution4 = "C({0},3)".format(ns)
  solution5 = "C({0},2)".format(ns)
  solution6 = "{1}*({1}-1)*C({0},3)*C({0},2)".format(ns,nr)
  solution7 = "{1}*({1}-1)*C({0},3)*C({0},2)/C({2},5)".format(ns,nr,n)
  
  solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7] 
  return solutions
