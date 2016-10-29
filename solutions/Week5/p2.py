import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  n = random.randrange(0,5,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  problem = [["mixture_cdf_1.png","-2.0", "0.5", "0.5", "-0.5", "0.5"]]
  problem += [["mixture_cdf_4.png","1.0", "1", "0.4", "2.5", "0.6"]]
  problem += [["mixture_cdf_13.png","0.5", "1.5", "0.25", "1.0", "0.75"]]
  problem += [["mixture_cdf_14.png","-2.0", "1", "0.35", "3.0", "0.65"]]
  problem += [["mixture_cdf_17.png","1.5", "1.5", "0.5", "0.0", "0.5"]]
  
  img_file, mean, solution1, solution2, solution3, solution4 = problem[n]
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4]  
  return solutions
