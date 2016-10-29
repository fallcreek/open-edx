import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  n = random.randrange(0,3,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  problem = [["mixture_cdf_7.png","1.0", "0.5", "0.65", "-4.5", "-2.5", "0.35"]]
  problem += [["mixture_cdf_11.png","-1.0", "1", "0.25", "-1.0", "2.0", "0.75"]]
  problem += [["mixture_cdf_12.png","1.0", "1", "0.3", "-3.0", "-1.0", "0.7"]]
  
  img_file, mean, solution1, solution2, solution3, solution4, solution5 = problem[n]
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4, solution5]  
  return solutions
