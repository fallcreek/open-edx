import random
def answer(seed):
  random.seed(seed)
  a = random.randrange(300,400,1)
  b = random.randrange(15,25,1)
  
  solution1 = "C(10,8) * 0.5^{10}"
  solution2 = "C(10,9) * 0.5^{10}"
  solution3 = "1 * 0.5^{10}"
  solution4 = "(C(10,8) +C(10,9) + 1) * 0.5^{10}"
  solution5 = "1- ((C(10,8) +C(10,9) + 1) * 0.5^{10})"
  solution6 = " ({{{0}}}) ^ {{{1}}}".format(solution5,a)
  solution7 = " 1 - ({0})".format(solution6)
  
  solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7]
  return solutions
