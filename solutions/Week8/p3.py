import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  x = random.randrange(8,10,1);
  X = x*x;
  y = random.randrange(1,5,1);
  t=random.randrange(1,4,1)
  lambd = 400./X;
  
  # for name in ['x','X','y','lambd','t']:
  #     print name,locals()[name]
  
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "400/{0}".format(X)
  solution2 = "e^{{(-400/{0})}}*(400/{0})^{{({1})}}/({1}!)".format(X,y)
  solution3 = "({0}*{0})*(e^{{(-400/{1})}}*(400/{1})^{{({2})}}/({2}!))".format(x,X,y)
  solution4 = "1-e^{{(-400/{0}*{1}/24)}}".format(X,t)
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4]
  return solutions
