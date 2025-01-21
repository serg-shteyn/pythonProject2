import unittest
from unittest import TestCase, main


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def __repr__(self):
        return self.name

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        pass
        # return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.key = 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        key = 1
        running = Tournament(90, self.run1, self.run3)
        self.all_results[key] = running.start()
        max_res = max(self.all_results[key])
        self.assertTrue(self.run3.name == self.all_results[key][max_res])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        key = 2
        running = Tournament(90, self.run2, self.run3)
        self.all_results[key] = running.start()
        max_res = max(self.all_results[key])
        self.assertTrue(self.run3.name == self.all_results[key][max_res])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        key = 3
        running = Tournament(90, self.run2, self.run1, self.run3)
        self.all_results[key] = running.start()
        max_res = max(self.all_results[key])
        self.assertTrue(self.run3.name == self.all_results[key][max_res])

    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results:
            print(cls.all_results[test])


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
	is_frozen = False

	@unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
	def test_walk(self):
		tw=Runner('Name1')
		for i in range(10):
			tw.walk()
		self.assertEqual(tw.distance,50)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_run(self):
	    tr=Runner('Name2')
	    for i in range(10):
	        tr.run()
	    self.assertEqual(tr.distance,100)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_challenge(self):
		tw=Runner('Name3')
		tr=Runner('Name4')
		for i in range(10):
			tw.walk()
			tr.run()
		self.assertNotEqual(tw.distance,tr.distance)

