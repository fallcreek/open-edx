import random
def answer(seed):
  random.seed(seed)
  # random variables (no need to import random library)
  def rand_vals(i=1,j=100,n=2):
      return [random.randrange(i,j,1) for k in range(n)]
  a_rand=rand_vals() ; b_rand=rand_vals() ; c_rand=rand_vals();
  a_vals=[]; b_vals=[]; c_vals=[];
  for i in range(len(a_rand)):
      for j in range(len(b_rand)):
          for k in range(len(c_rand)):
              a_vals.append(a_rand[i])
              b_vals.append(b_rand[j])
              c_vals.append(c_rand[k])
  variable_values = {'a':a_vals, 'b':b_vals, 'v':c_vals}
  
  # Random valued coefficients:
  [c,d,e,f,g]=rand_vals(i=2,j=5,n=5)
  
  # Solutions with variables converted to string
  # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1. 
  solution1 = "{0}*a".format(c)
  solution2 = "{0}*a+{1}*b+{2}".format(c,d,e)
  solution3 = "-{0}*a+{1}*b+{2}*{3}*v-1".format(c,d,c,d) 
  
  # Group all solutions into a list
  solutions = [solution1, solution2, solution3]
  return solutions
