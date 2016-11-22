import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  
  k = 0.0+random.randrange(1,2,1);
  r = 0.0+random.randrange(1,2,1);
  a = 0.0+random.randrange(800,1200,100);
  select = 0.0+random.randrange(8,15,1);
  s = (1.*a)/10;
  
  j = 0.0+random.randrange(1,3,1);
  
  x = 0.0+random.randrange(12,15,1);
  y = 0.0+random.randrange(5,6,1);
  
  # for name in ['k','r','a','select','s','j','x','y']:
  #     print name,locals()[name]
  
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "{0}*1/{1}".format(s,a)
  solution2 = "e^{{(-.1)}}*(.1)^{{({0})}}/{0}!".format(j)
  solution3 = "e^{{(-{0}/{1})}}".format(s, a)
  
  # Group all solutions into a list
  solutions = [solution1,solution2,solution3]
  return solutions
