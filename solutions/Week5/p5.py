import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  
  n = 2*random.randrange(40,50,1)
  m = n-1
  
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  solution1 = "(0.5*0)+(0.5*1)"
  solution2 = "(0.5*(0-0.5)^2)+(0.5*(1-0.5)^2)"
  solution3 = "0.5-0.5"
  solution4 = "0.25+0.25"
  solution5 = "0.5-(2*0.5)+0.5"
  solution6 = "0.25+(4*0.25)+0.25"
  solution7 = "0"
  solution8 = "{0}*0.25".format(n)
  
  # Group all solutions into a list
  solutions = [solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]  
  return solutions
