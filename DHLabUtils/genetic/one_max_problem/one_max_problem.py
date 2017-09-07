import numpy as np
from ..evo_alg import Problem


class OneMaxProblem(Problem):
    def __init__(self, length=200):
        self.length = length


    def get_random_solution(self):
        return np.random.choice([0, 1], size=(self.length,))

    def fitness_function(self, solution):
        return sum(solution)

    def mate(self, sol1, sol2):
        newSol = []
        for n in range(len(sol1)):
            newSol.append(np.random.choice([sol1[n], sol2[n]]))
        return newSol
