import random
def answer(seed):
    random.seed(seed)
     # random variables (no need to import random library)
    p_men = random.randrange(6,8,1)
    p_women = random.randrange(3,5,1)
    
    # Solutions with variables converted to string
    # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
    solution1 = "{0}/100*0.5".format(p_men)
    solution2 = "{0}/100*0.5+{1}/100*0.5".format(p_men,p_women)
    solution3 = "({0})/({1})".format(solution1,solution2)
    
    # Group all solutions into a list
    solutions = [solution1,solution2,solution3]
    return solutions
