import random
def answer(seed):
  random.seed(seed)
  import math
  
  def combination(n,k):
      return math.factorial(n)/(math.factorial(n - k) * math.factorial(k))
  
  nCards=random.randrange(4,7,1)
  b=random.randrange(2,nCards-1,1)
  c = nCards-b
  
  solution1 = "C(52,{0})".format(nCards)
  solution2 = "4"
  solution3 = "C(13,{0})".format(b)
  solution4 = "52 - 13"
  solution5 = "C(39, {1} - {0})".format(b,nCards)
  solution6 = "4*C(13,{0})*C(39,{1}-{0})".format(b,nCards)
  solution7 = "4*C(13,{0})*C(39,{1}-{0})/C(52,{1})".format(b,nCards)
  
  solutions = [solution1,solution2,solution3,solution4,solution5,solution6, solution7]
  return solutions
