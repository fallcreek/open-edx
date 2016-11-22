import random
def answer(seed):
  random.seed(seed)
  
  r = random.randrange(4,6,1)/10.0;#random(0.4,0.6,0.1);
  k = random.randrange(100,200,1);
  
  p = random.randrange(r*10+1,9,1)/10.0#random(r+0.1,0.9,0.1);
  n2 = random.randrange(300,500,1);
  k2 = random.randrange(251,299,1);
  #ans1 = ceil(p*k/r);
  
  solution1 = "{0}*{1}/{2}".format(p, k, r) #{Compute("$p*$k/$r")}
  solution2 = "{0}*{1}/{2}".format(n2, r, k2) #{Compute("$n2*$r/$k2")->with(tolType=>'absolute', tolerance=>'0.01')}
  
  solutions = [solution1, solution2]  
  return solutions
