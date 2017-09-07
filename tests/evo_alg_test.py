
import unittest

from ..DHLabUtils.genetic.evo_alg import *
from ..DHLabUtils.genetic.one_max_problem import *

class TestEvoAlg(unittest.TestCase):

    def test_get_fittest(self):
        """
        Test of we get the fittest from a list of number. Which in this case are the highest numbers
        :return:
        """
        pop = [1,2,3,4,5,6,7,8,9,10,11,11,12,15]
        def fitnessFunction(individual):
            return individual
        top_5 = [15,12,11,11,10]
        self.assertEqual(getFittest(pop, fitnessFunction, 5), top_5)

    def test_with_one_max(self):
        """
        Test wether evolution algorithm works with one max.
        """
        problem = OneMaxProblem(100)
        solution = get_solution(problem, 500, 100, 50)
        self.assertEqual(problem.fitness_function(solution), 100)


