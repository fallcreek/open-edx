import random
def answer(seed):
  random.seed(seed)
  k = random.randrange(6,10,1);
  t1 = random.randrange(2,5,1);
  t2 = random.randrange(2,5,1);
  r = random.randrange(1,6,1)/10.0; #random(0.1,0.6,0.1);
  
  solution1 = "{0}*({0}+1)/(2*{0})".format(k);
  solution2 = "2*{0}/({0}+1) + ({0}*({0}-1))/(2*({0}+1))".format(k);
  solution3 = "{0}*{2} + {1}*({3})".format(t1,t2,solution1,solution2);
  solution4 = "({0})/{1}".format(solution3,r);
  
  solutions = [solution1, solution2, solution3, solution4]  
  return solutions
