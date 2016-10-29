import random
def answer(seed):
  random.seed(seed)
  a = random.randrange(4,6,1)
  
  if (a == 4):
      lts = "AABBCC";
      solution2 = "6!/2^3"
  
  if (a == 5):
      lts = "AAABBC";
      solution2 = "6!/(3!*2!)"
  
  if (a == 6):
      lts = "AABCD"
      solution2 = "5!/2"
  
  solution1 = "4!/(2*2)"
  solutions = [solution1, solution2]    
  return solutions
