import random
def answer(seed):
    random.seed(seed)
    n = random.choice(range(13,16,1))
    x = random.choice(range(2,9,1))
    y = random.choice(range(x+2,13,1))
    # Solutions with variables converted to string
    # Make sure you name the solution with part id at the end. e.g. 'solution1' will be solution for part 1.
    solution1 = "{0}-1".format(n)
    solution2 = "{0}-2".format(n)
    solution3 = "({0}-1)*({0}-2)".format(n)
    solution4 = "{0} - {1} - 1".format(y, x)
    solution5 = "({0}-{1})*({0}-{1}-1)/2".format(n,x)
    solution6 = "1 * ({0}-{1})*({0}-{1}-1)/2/(({0}-1)*({0}-2))".format(n,x)
    
    
    # Group all solutions into a list
    solutions = [solution1, solution2, solution3, solution4, solution5, solution6]
    return solutions
