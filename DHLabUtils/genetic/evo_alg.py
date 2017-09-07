import random
from abc import abstractmethod
import numpy as np

def getFittest(pop, fitness_function, n):
    return sorted(pop, key=lambda individual: fitness_function(individual), reverse=True)[0:n]

def mate(population, mate_function, sizePop):
    """
    Function that creates offsprings in the new population
    :param population:
    :param mate_function:
    :param sizePop:
    :return:
    """
    new_pop = []
    for n in range(0,sizePop):
        #improvement make selecting the same individual impossible
        new_pop.append(mate_function(random.choice(population), random.choice(population)))
    return new_pop


def get_solution(P, number_of_generations, population_size, surviving, fresh_pop=10):
    """
    Gets a solution from the problem
    :param P: The problem that you want to solve
    :param number_of_generations: The number generations that will be created
    :param population_size: The size of each population
    :param surviving: How many of fittest should survive for the next generation
    :param fresh_pop: How many random "fresh" solutions each generation should introduce
    :return:
    """
    pop = P.get_random_solutions(population_size)
    best = None
    for gen in range(0, number_of_generations):
        fittest = getFittest(pop, P.fitness_function, surviving)
        freshPop =P.get_random_solutions(fresh_pop)
        fittest += freshPop
        pop = mate(fittest, P.mate, population_size)
        best = fittest[0]
    return best

class Problem:
    """
    A class that describes how a problem should look like
    """
    @abstractmethod
    def get_random_solution(self):
        pass

    def get_random_solutions(self, n):
        return [self.get_random_solution() for i in range(0, n)]

    @abstractmethod
    def fitness_function(self, solution):
        pass

    @abstractmethod
    def mate(self, sol1, sol2):
        pass








