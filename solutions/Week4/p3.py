import random
def answer(seed):
    random.seed(seed)
    # random variables (no need to import random library)
    #false burglary percentage
    atpt = random.randrange(92,96,1)
    perc=atpt/100
    
    #burglary percentage
    fals = random.randrange(1,3,1)
    fperc = fals/100
    
    # Solutions with variables converted to string
    # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
    solution1 = "1/10000"
    solution2 = "{0}/10000 + {1}*(1-1/10000)".format(perc, fperc)
    solution3 = "{0}/10000".format(perc)
    solution4 = "({1})/({0})".format(solution2,solution3)
    
    # Group all solutions into a list
    solutions = [solution1, solution2, solution3, solution4]
    return solutions
