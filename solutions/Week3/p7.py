import random
def answer(seed):
  random.seed(seed)
  from math import sqrt
  from math import exp
  from math import factorial as f
  
  def cnk(n, k):
      return int(f(n)/f(k)/f(n-k))
  
  def pmt(n, k):
      return int(f(n)/f(n-k))
  Tk = [1,2,3,2,5,7,9]
  Tn = [3,3,3,10,10,10,10]
  t = random.randrange(0,7,1)
  n = Tn[t]
  k = Tk[t]
  
  R1=random.randrange(5,20,1)  # Number of balls (both white and black)
  R2=random.randrange(2,R1-1,1)  # Number of white balls
  R3=R1-R2 # Number of black balls
  
  solution1 = "{0}!/({1}!*({0}-{1})!)".format(R1,R2)
  
  solutions = [solution1]
  return solutions
