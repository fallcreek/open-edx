import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  n = random.randrange(0,8,1)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
  problem = [["mixture_cdf_0.png","1.0", "0.7", "1.0", "3.5", "0.3"]]
  problem += [["mixture_cdf_2.png","0.5", "0.4", "2.0", "3.5", "0.6"]]
  problem += [["mixture_cdf_6.png","1.0", "0.55", "-0.5", "2.5", "0.45"]]
  problem += [["mixture_cdf_8.png","1.5", "0.3", "4.0", "4.5", "0.7"]]
  problem += [["mixture_cdf_9.png","1.5", "0.6", "-2.5", "4.5", "0.4"]]
  problem += [["mixture_cdf_16.png","0.5", "0.65", "-1.5", "4.5", "0.35"]]
  problem += [["mixture_cdf_18.png","1.5", "0.55", "-4.5", "-2.0", "0.45"]]
  problem += [["mixture_cdf_19.png","0.5", "0.6", "1.5", "3.5", "0.4"]]
  img_file, lam, solution1, solution2, solution3, solution4 = problem[n]
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4]
  
  return solutions
