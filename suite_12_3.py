# Систематизация и пропуск тестов

# Часть 1. TestSuit.
from tests_12_3 import TournamentTest,RunnerTest
import unittest

testRT = unittest.TestSuite()
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runer_tests = unittest.TextTestRunner(verbosity=2)
runer_tests.run(testRT)

# Часть 2. Пропуск тестов.

