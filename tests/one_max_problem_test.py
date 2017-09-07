

import unittest

from ..DHLabUtils.genetic.evo_alg import *
from ..DHLabUtils.genetic.one_max_problem import OneMaxProblem


class TestOneMaxProblem(unittest.TestCase):

    def setUp(self):
        self.P = OneMaxProblem(100)

    def test_fitness(self):
        solution = [1,1,1,0]
        self.assertEqual(self.P.fitness_function(solution), 3)

    def test_mate(self):
        sol1 = self.P.get_random_solution()
        sol2 = self.P.get_random_solution()
        sol3 = self.P.mate(sol1, sol2)
        self.assertEqual(len(sol3), 100)

    def test_get_random_solutions(self):
        solutions = self.P.get_random_solutions(200)
        self.assertEqual(len(solutions), 200)
