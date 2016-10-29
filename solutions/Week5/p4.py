import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  n = random.randrange(0,4,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  problem = [["mixture_cdf_3.png","0.5", "0.25", "-2.5", "0.75"]]
  problem += [["mixture_cdf_5.png","0.5", "0.45", "2.5", "0.55"]]
  problem += [["mixture_cdf_10.png","1.0", "0.3", "2.0", "0.7"]]
  problem += [["mixture_cdf_15.png","0.5", "0.3", "-0.5", "0.7"]]
  img_file, lam, solution1, solution2, solution3 = problem[n]
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3]  
  return solutions
