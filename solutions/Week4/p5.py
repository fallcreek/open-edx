import random
def answer(seed):
    solution1 = "4^2"
    solution2 = "C(52-5,2) - C(52-5-4,2)"
    solution3 = "C(52-5,2)"
    solution4 = "(C(52-5,2) - C(52-5-4,2) + 4^2) / C(52-5,2)"
    
    
    # Group all solutions into a list
    solutions = [solution1, solution2, solution3, solution4]

    return solutions
