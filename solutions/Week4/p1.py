import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  pa = random.randrange(1,6,1)/10.
  pb = random.randrange(1,6,1)/10.
  is_indep=(random.random()>0.5)*1
  
  if is_indep == 1:
      paub=pa+pb-pa*pb
  else:
      paub=pa+pb-pa*pb*2
  
  solution1="{0} + {1} - ({2})".format(pa,pb,paub)
  solution2="({0})/{1}".format(solution1,pb)
  solution3= str(is_indep)
  solutions = [solution1,solution2,solution3]
  return solutions
