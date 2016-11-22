import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  def rand_vals(i=1,j=100,n=3):
      return [random.randrange(i,j,1) for k in range(n)]
  a_rand=rand_vals() ; b_rand=rand_vals(n=2)
  a_vals=[]; b_vals=[];
  for i in range(len(a_rand)):
      for j in range(len(b_rand)):
          a_vals.append(a_rand[i])
          b_vals.append(b_rand[j])
  variable_values = {'a':a_vals, 'b':b_vals}
  
  # Random valued coefficients:
  [c,d,e]=rand_vals(i=2,j=8,n=3)
  
  #index_of_test_value = 2 #should not be used.
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
  solution1 = "{0}*a-{0}*a".format(c)
  solution2 = "{0}*a-{0}*a".format(c)
  solution3 = "{0}*a-{1}*a".format(c,d)
  solution4 = "(({0})^2)*b".format(c)
  solution5 = "2*(({0})^2)*b".format(c,d)
  solution6 = "0"
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3, solution4, solution5, solution6]
  return solutions
